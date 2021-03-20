from flask import abort
from sqlalchemy.exc import IntegrityError, PendingRollbackError, NoResultFound

from application.models import Color
from application.models import db


def read_all():
    """Returns the whole list of colors from the database."""
    colors = db.session.query(Color).all()
    return [c.serialize for c in colors]


def read_one(color_name):
    """Returns a single color from the database."""
    try:
        color = db.session.query(Color).filter_by(color=color_name).one()
        return color.serialize
    except NoResultFound:
        return abort(404, f"color '{color_name}' not found")


def create(body):
    """Inserts a new color into the database."""
    new_color = Color(color=body['color'], value=body['value'])
    try:
        db.session.add(new_color)
        db.session.commit()
        return new_color.serialize, 201
    except (IntegrityError, PendingRollbackError):
        db.session.rollback()
        return abort(400, f"color '{body['color']}' already exists in the database.")
