from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError, PendingRollbackError

from database_setup import Base, Color

import json

# Database session setup
engine = create_engine('sqlite:///colors.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Import entries from colors.json into the database
with open('colors.json', 'r') as colors_file:
    colors = json.load(colors_file)
    # If at least one entry from the colors.json file already exists in the database, an exception will be thrown and
    # it's assumed that the database has been initialized before.
    try:
        for color_entry in colors:
            color = color_entry['color']
            value = color_entry['value']
            newColor = Color(color=color, value=value)
            session.add(newColor)
            session.commit()
        print("The colors.db database has been successfully initialized with the entries from the colors.json file.")
    except (IntegrityError, PendingRollbackError):
        print("One of the entries already found in the database, it has been probably initialized before.")
        session.rollback()
