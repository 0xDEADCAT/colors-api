import pytest
from sqlalchemy.exc import SAWarning
from werkzeug.exceptions import BadRequest, NotFound

from application.colors import read_all, read_one, create


def test_read_all_empty_database(init_empty_database):
    """
    GIVEN an empty Colors table in the database
    WHEN attempting to retrieve the whole list of colors
    THEN an empty list is returned
    """
    colors_list = read_all()
    assert len(colors_list) == 0
    assert isinstance(colors_list, list)


def test_read_all(init_database, colors_list):
    """
    GIVEN a Colors table with three colors: 'red', 'green', 'blue' in the database
    WHEN attempting to retrieve the whole list of colors
    THEN a list containing three dicts: {'color': 'red', 'value': '#f00'},
                                        {'color': 'green', 'value': '#0f0'},
                                        {'color': 'blue', 'value': '#00f'} should be returned
    """
    returned_colors_list = read_all()
    print(returned_colors_list)
    assert len(returned_colors_list) == 3
    assert isinstance(returned_colors_list, list)
    for index, color in enumerate(returned_colors_list):
        assert color['color'] == colors_list[index]['color']
        assert color['value'] == colors_list[index]['value']


def test_read_one(init_database, color_red):
    """
    GIVEN a Colors table with three colors: 'red', 'green', 'blue' in the database
    WHEN attempting to retrieve the color 'red'
    THEN a dict {'color': 'red', 'value': '#f00'} should be returned
    """
    returned_color = read_one('red')
    assert isinstance(returned_color, dict)
    assert returned_color['color'] == color_red['color']
    assert returned_color['value'] == color_red['value']


def test_read_one_non_existing_color(init_database):
    """
    GIVEN a Colors table with three colors: 'red', 'green', 'blue' in the database
    WHEN attempting to retrieve the color 'purple'
    THEN a NotFound exception should be raised
    """
    color = 'purple'
    with pytest.raises(NotFound) as e:
        assert read_one(color)
    assert str(e.value) == f"404 Not Found: color '{color}' not found"


def test_create(init_empty_database, color_red):
    """
    GIVEN an empty Colors table in the database
    WHEN attempting to insert the dict {'color': 'red', 'value': '#f00'} in that table
    THEN the color should be created in the database and a tuple containing the
         dict {'color': 'red', 'value': '#f00'} and status code 201 should be returned
    """
    returned_color, status_code = create(color_red)
    assert isinstance(returned_color, dict)
    assert returned_color['color'] == color_red['color']
    assert returned_color['value'] == color_red['value']
    assert status_code == 201


def test_create_duplicate(init_database, color_red):
    """
    GIVEN a Colors table with three colors: 'red', 'green', 'blue' in the database
    WHEN attempting to insert the dict {'color': 'red', 'value': '#f00'} in that table
    THEN an IntegrityError exception should be raised
    """
    with pytest.raises(BadRequest) as e:
        with pytest.warns(SAWarning):
            assert create(color_red)
    assert str(e.value) == f"400 Bad Request: color '{color_red['color']}' already exists in the database."
