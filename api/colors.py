from connexion import problem

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, PendingRollbackError, NoResultFound
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import SingletonThreadPool

from database_setup import Base, Color

# Connect to database and create session
engine = create_engine('sqlite:///colors.db', poolclass=SingletonThreadPool, connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def read_all():
    """Returns the whole list of colors from the database."""
    colors = session.query(Color).all()
    return [c.serialize for c in colors]


def read_one(color_name):
    """Returns a single color from the database."""
    try:
        color = session.query(Color).filter_by(color=color_name).one()
        return color.serialize
    except NoResultFound:
        return problem(404, 'Not Found', f"color '{color_name}' not found")


def create(body):
    """Inserts a new color into the database."""
    new_color = Color(color=body['color'], value=body['value'])
    try:
        session.add(new_color)
        session.commit()
        return new_color.serialize, 201
    except (IntegrityError, PendingRollbackError):
        session.rollback()
        return problem(400, 'Bad Request', f"color '{body['color']}' already exists in the database.")
