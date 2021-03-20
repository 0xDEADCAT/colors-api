from application import create_app

from config import Config

# uWSGI looks for 'application' by default
application = create_app(Config)

if __name__ == '__main__':
    application.run(debug=True)
