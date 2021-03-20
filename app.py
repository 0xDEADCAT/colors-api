from flask import redirect

import config

# Get the application instance
connex_app = config.connex_app

# Read the colors.yaml file to configure the endpoints
connex_app.add_api('colors.yaml')


# Redirect from root path to Swagger UI
@connex_app.route('/')
def redirect_to_swagger_ui():
    """This function responds to the browser URL
    localhost:5000/ and redirects to Swagger UI

    :return:    redirect to '/ui'
    """
    return redirect('/ui')


if __name__ == '__main__':
    connex_app.run()
