import pytest
from flask import url_for


def test_read_all_colors_empty(client, init_empty_database):
    response = client.get(url_for('/api.application_colors_read_all'))
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) == 0


def test_read_all_colors(client, init_database):
    expected_colors_list = [{'color': 'red', 'value': '#f00'},
                            {'color': 'green', 'value': '#0f0'},
                            {'color': 'blue', 'value': '#00f'}]
    response = client.get(url_for('/api.application_colors_read_all'))
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) == 3
    for index, color in enumerate(response.json):
        assert color['color'] == expected_colors_list[index]['color']
        assert color['value'] == expected_colors_list[index]['value']


def test_read_one_color(client, init_database):
    color_red = {'color': 'red', 'value': '#f00'}
    response = client.get(url_for('/api.application_colors_read_one', color_name=color_red['color']))
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert response.json == color_red


def test_read_one_color_with_invalid_name(client, init_empty_database):
    color_name = 'white3'
    response = client.get(url_for('/api.application_colors_read_one', color_name=color_name))
    assert response.status_code == 400
    assert isinstance(response.json, dict)
    assert f"'{color_name}' does not match" in response.json['detail']


def test_read_one_non_existing_color(client, init_empty_database):
    color_red = {'color': 'red', 'value': '#f00'}
    response = client.get(url_for('/api.application_colors_read_one', color_name=color_red['color']))
    assert response.status_code == 404
    assert isinstance(response.json, dict)
    assert f"color '{color_red['color']}' not found"


def test_create_color(client, init_empty_database):
    color_red = {'color': 'red', 'value': '#f00'}
    response = client.post(url_for('/api.application_colors_create'), json=color_red)
    assert response.status_code == 201
    assert isinstance(response.json, dict)
    assert response.json == color_red


def test_create_color_missing_color_field(client, init_empty_database):
    color_red = {'value': '#f00'}
    response = client.post(url_for('/api.application_colors_create'), json=color_red)
    assert response.status_code == 400
    assert isinstance(response.json, dict)
    assert response.json['detail'] == "'color' is a required property"


@pytest.mark.parametrize('test_color_name', ['r ed', 're d', 're3', 'red3', 'red#', 'bloody_red'])
def test_create_color_incorrect_color_name_format(client, init_empty_database, test_color_name):
    color_red = {'color': test_color_name, 'value': '#f00'}
    response = client.post(url_for('/api.application_colors_create'), json=color_red)
    assert response.status_code == 400
    assert isinstance(response.json, dict)
    assert f"'{test_color_name}' does not match" in response.json['detail']


@pytest.mark.parametrize('test_color_name', ['', 'r', 're'])
def test_create_color_incorrect_color_name_length(client, init_empty_database, test_color_name):
    color_red = {'color': test_color_name, 'value': '#f00'}
    response = client.post(url_for('/api.application_colors_create'), json=color_red)
    assert response.status_code == 400
    assert isinstance(response.json, dict)
    assert f"'{test_color_name}' is too short" in response.json['detail']


def test_create_color_missing_value_field(client, init_empty_database):
    color_red = {'color': 'red'}
    response = client.post(url_for('/api.application_colors_create'), json=color_red)
    assert response.status_code == 400
    assert isinstance(response.json, dict)
    assert response.json['detail'] == "'value' is a required property"


@pytest.mark.parametrize('test_value', ['', ' ', 'f', 'f0', 'f00', 'ff0000', '#', '#f', '#f0', '#f000', '#f0000',
                                        '#ff00000', 'f#f00', 'f#ff0000'])
def test_create_color_incorrect_value_format(client, init_empty_database, test_value):
    color_red = {'color': 'red', 'value': test_value}
    response = client.post(url_for('/api.application_colors_create'), json=color_red)
    assert response.status_code == 400
    assert isinstance(response.json, dict)
    assert f"'{test_value}' does not match" in response.json['detail']
