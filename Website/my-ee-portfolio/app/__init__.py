from flask import Flask


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_mapping(
        SECRET_KEY="your_secret_key", DATABASE="path_to_your_database"
    )

    from app.routes import main

    app.register_blueprint(main)

    return app
