from flask import Flask, jsonify, request

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, PendingRollbackError, NoResultFound
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import SingletonThreadPool

import re

from database_setup import Base, Color

app = Flask(__name__)

# Connect to database and create session
engine = create_engine('sqlite:///colors.db', poolclass=SingletonThreadPool, connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Regex pattern for the color value
color_value_pattern = re.compile(r'^#[0-9a-f]{3}$')


def get_colors():
    colors = session.query(Color).all()
    return jsonify([c.serialize for c in colors])


def get_color(color_name):
    try:
        color = session.query(Color).filter_by(color=color_name).one()
        return jsonify(color.serialize)
    except NoResultFound:
        return jsonify(error='No color with the given name exists.')


def create_color(color_name, color_value):
    # Check if the color_value format is valid
    if color_value_pattern.match(color_value):
        new_color = Color(color=color_name, value=color_value)
        try:
            session.add(new_color)
            session.commit()
            return jsonify(new_color.serialize)
        except (IntegrityError, PendingRollbackError):
            session.rollback()
            return jsonify(error='Color with that name already exists in the database.')
    else:
        return jsonify(error='Format of the color value is incorrect.')


@app.route('/')
@app.route('/colors/', methods=['GET', 'POST'])
def colors_endpoint():
    if request.method == 'GET':
        return get_colors()
    elif request.method == 'POST':
        color_json = request.get_json()
        color_name = color_json['color'].strip().lower()
        color_value = color_json['value'].strip().lower()
        if color_name and color_value:
            return create_color(color_name=color_name, color_value=color_value)
        else:
            error_msg = f'The color name and value cannot be empty.' if not color_name and not color_value \
                else f'The color name cannot be empty.' if not color_name else f'The color value cannot be empty.'
            return jsonify(error=error_msg)


@app.route('/colors/<color_name>')
def color_endpoint(color_name):
    return get_color(color_name=color_name)


if __name__ == '__main__':
    app.run()
