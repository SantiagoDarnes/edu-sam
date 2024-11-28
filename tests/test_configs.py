from app import create_app
import os

def test_secret_github():
    assert create_app().config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")