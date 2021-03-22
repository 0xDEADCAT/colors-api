from application.models import Color


def test_new_color(color_red):
    """
    GIVEN a Color model
    WHEN a new Color is created
    THEN check if the color_name and color_value fields are defined correctly
    """
    color = Color(color=color_red['color'], value=color_red['value'])
    assert color.color == color_red['color']
    assert color.value == color_red['value']


def test_serialization(color_red):
    """
    GIVEN a Color model
    WHEN the Color is serialized
    THEN the returned dictionary should contain 'color' and 'value' fields with proper values
    """
    color = Color(color=color_red['color'], value=color_red['value'])
    color_serialized = color.serialize
    assert color_serialized['color'] == color_red['color']
    assert color_serialized['value'] == color_red['value']
