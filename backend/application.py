import os

from flask import Flask
from flask_cors import CORS

from db import db
from marsh import ma


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "SQLALCHEMY_DATABASE_URI", "postgresql://tcell:bronx@localhost/bronx"
    )

    db.init_app(app)
    ma.init_app(app)
    CORS(app)

    return app
