import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Connexion
    SPECIFICATION_DIR = os.path.join(basedir, 'openapi/')
    SPECIFICATION_FILE = 'colors.yaml'

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'application/colors.db')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
