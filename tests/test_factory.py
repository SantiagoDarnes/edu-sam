from app import create_app
import os

def test_config():
    assert os.environ.get('DATABASE_URL') in create_app().config["SQLALCHEMY_DATABASE_URI"]
    assert os.environ.get('SECRET_KEY') in create_app().config["SECRET_KEY"]