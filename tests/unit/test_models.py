from application.models import Color


def test_new_color():
    """
    GIVEN a Color model
    WHEN a new Color is created
    THEN check if the color_name and color_value fields are defined correctly
    """
    color_name = 'red'
    color_value = '#f00'
    color = Color(color=color_name, value=color_value)
    assert color.color == color_name
    assert color.value == color_value


def test_serialization():
    """
    GIVEN a Color model
    WHEN the Color is serialized
    THEN the returned dictionary should contain 'color' and 'value' fields with proper values
    """
    color_name = 'red'
    color_value = '#f00'
    color = Color(color=color_name, value=color_value)
    color_serialized = color.serialize
    assert color_serialized['color'] == color_name
    assert color_serialized['value'] == color_value
