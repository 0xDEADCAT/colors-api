import connexion


def create_app(config_obj):
    # Create the Connexion application instance
    connex_app = connexion.App(__name__, specification_dir=config_obj.SPECIFICATION_DIR)

    # Read the specification file to configure the endpoints
    connex_app.add_api(config_obj.SPECIFICATION_FILE)

    # Get the underlying Flask app instance
    app = connex_app.app
    app.config.from_object(config_obj)

    # Initialize database plugin
    from application.models import db
    db.init_app(app)

    with app.app_context():
        # Include routes
        from . import routes

        # Register blueprints
        app.register_blueprint(routes.main_bp)

        return connex_app
