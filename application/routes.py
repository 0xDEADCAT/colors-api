from flask import Blueprint, redirect, url_for

# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__
)


# Redirect from root path to Swagger UI
@main_bp.route('/')
def redirect_to_swagger_ui():
    """This function responds to the browser URL
    localhost:5000/ and redirects to Swagger UI

    :return:    redirect to '/ui'
    """
    return redirect(url_for('/api./api_swagger_ui_index'))
