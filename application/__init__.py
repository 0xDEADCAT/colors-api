import connexion

from config import Config


def create_app():
    # Create the Connexion application instance
    connex_app = connexion.App(__name__, specification_dir=Config.SPECIFICATION_DIR)

    # Read the specification file to configure the endpoints
    connex_app.add_api(Config.SPECIFICATION_FILE)

    # Get the underlying Flask app instance
    app = connex_app.app
    app.config.from_object(Config)

    # Initialize database plugin
    from application.models import db
    db.init_app(app)

    with app.app_context():
        # Include routes
        from . import routes

        # Register blueprints
        app.register_blueprint(routes.main_bp)

        return connex_app
