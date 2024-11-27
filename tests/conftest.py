import tempfile, os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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


class AuthActions:
    def __init__(self, test_client):
        self._client = test_client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/login',
            data={'username': username, 'password': password}
        )
    
    def logout(self):
        return self._client.get('/login/logout')
    
@pytest.fixture()
def auth(client):
    return AuthActions(client)