import os

from flask import Flask
from flask_restx import Api

from .models import db, migrate
from .views import oauth_namespace

from dotenv import load_dotenv
load_dotenv('.env') 


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oauth.db'

    db.init_app(app)
    migrate.init_app(app, db)

    api = Api(
        app,
        title="Simple OAuth Service",
        description="A REST API for authenticating with OAuth")

    api.add_namespace(oauth_namespace, path="")

    with app.app_context():
        db.create_all()

    return app