from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "thematic project"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{path.join(path.abspath('website'), DB_NAME)}"# Telling flask where my db is stored
    db.init_app(app)

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note
    create_database(app)
    
    return app

def create_database(app):
    db_path = path.join(path.abspath('website'), DB_NAME)
    if not path.exists(db_path):            # If database doesn't exist,
        with app.app_context():             # create it.
            db.create_all()  
            print("Created Database!")