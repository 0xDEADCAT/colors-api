from application import create_app

# uWSGI looks for 'application' by default
application = create_app()

if __name__ == '__main__':
    application.run(debug=True)
