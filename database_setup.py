import json
import os

from config import db
from models import Color

# Delete database file if it exists currently
if os.path.exists('colors.db'):
    os.remove('colors.db')

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
