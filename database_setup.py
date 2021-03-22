import json
import os

from application import create_app
from application.models import Color
from application.models import db

from config import Config

# Delete database file if it exists currently
db_file = ''.join(Config.SQLALCHEMY_DATABASE_URI.split('sqlite:///'))
if os.path.exists(db_file):
    os.remove(db_file)

connex_app = create_app(Config)
app = connex_app.app
app.app_context().push()

# Create the database
db.create_all()

# Import entries from colors.json and populate the database
with open('colors.json', 'r') as colors_file:
    colors = json.load(colors_file)
    # If at least one entry from the colors.json file already exists in the database, an exception will be thrown and
    # it's assumed that the database has been initialized before.
    for color_entry in colors:
        color = color_entry['color']
        value = color_entry['value']
        newColor = Color(color=color, value=value)
        db.session.add(newColor)
    db.session.commit()
    print("The colors.db database has been successfully initialized with the entries from the colors.json file.")
