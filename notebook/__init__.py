from .notes import NoteBook
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    os.makedirs(app.instance_path, exist_ok=True)
    db_path = os.path.join(app.instance_path, 'db.sqlite')
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path
    db.init_app(app)

    with app.app_context():
        from notebook import routes
        db.create_all()

    return app

