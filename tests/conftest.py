import pytest
from app import create_app, db
from flask import Flask

@pytest.fixture()
def app():
    app: Flask = create_app()
    app.config.update({
        'TESTING': True,
    })

    yield app

    with app.app_context():
        db.session.remove()
        db.engine.dispose()

@pytest.fixture()
def test_client(app: Flask):
    return app.test_client()

@pytest.fixture()
def runner(app: Flask):
    return app.test_cli_runner()
