from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/seed_data_development'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    app.config['SQLALCHEMY_ECHO'] = True
    app.url_map.strict_slashes = False

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import simple_book, book, author
    app.register_blueprint(simple_book.bp)
    app.register_blueprint(book.bp)
    app.register_blueprint(author.bp)

    return app
    