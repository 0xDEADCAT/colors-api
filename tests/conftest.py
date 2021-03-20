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
def init_database(app):
    with app.app_context():
        # Create the database
        db.create_all()

        # Insert color data
        color_red = Color(color='red', value='#f00')
        color_green = Color(color='green', value='#0f0')
        color_blue = Color(color='blue', value='#00f')
        db.session.add(color_red)
        db.session.add(color_green)
        db.session.add(color_blue)

        # Commit the changes
        db.session.commit()

        yield  # tests run here

        # Destroy the database
        db.drop_all()
