from flask import url_for


def test_redirect_to_swagger_ui(client):
    response = client.get(url_for('main_bp.redirect_to_swagger_ui'), follow_redirects=True)
    assert response.status_code == 200
    assert b"Swagger UI" in response.data
