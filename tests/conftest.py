import pytest
from flask import Flask
from flask.testing import FlaskClient

from flask_rest_test import create_app


@pytest.fixture()
def app() -> Flask:
    return create_app({"TESTING": True, "DEBUG": True})


@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()
