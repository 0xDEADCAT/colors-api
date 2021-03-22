import pytest

from application import create_app
from application.models import db, Color
from config import TestConfig


@pytest.fixture(scope='module')
def app():
    connex_app = create_app(TestConfig)
    return connex_app.app


@pytest.fixture()
def init_empty_database(app):
    with app.app_context():
        # Create the database
        db.create_all()

        yield  # tests run here

        # Destroy the database
        db.drop_all()


@pytest.fixture()
def init_database(app, colors_list):
    with app.app_context():
        # Create the database
        db.create_all()

        # Insert color data
        for color in colors_list:
            db.session.add(Color(color=color['color'], value=color['value']))

        # Commit the changes
        db.session.commit()

        yield  # tests run here

        # Destroy the database
        db.drop_all()


@pytest.fixture()
def color_red():
    return {'color': 'red', 'value': '#f00'}


@pytest.fixture()
def color_green():
    return {'color': 'green', 'value': '#0f0'}


@pytest.fixture
def color_blue():
    return {'color': 'blue', 'value': '#00f'}


@pytest.fixture()
def colors_list(color_red, color_green, color_blue):
    return [color_red, color_green, color_blue]
