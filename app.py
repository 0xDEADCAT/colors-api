import connexion
from flask import redirect

# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir='openapi/')

# Read the colors.yaml file to configure the endpoints
app.add_api('colors.yaml')


# Redirect from root path to Swagger UI
@app.route('/')
def redirect_to_swagger_ui():
    return redirect('/ui')


if __name__ == '__main__':
    app.run()
