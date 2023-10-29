import json

from flask import Flask
from flask.testing import FlaskClient

from flask_rest_test.db import app_db
from flask_rest_test.sandwich import Sandwich


def test_add_sandwich_adds_sandwich(client: FlaskClient, app: Flask):
    post_res = client.post(
        "/add", data=json.dumps({"id": 1, "name": "cheese", "count": "10"}), content_type="application/json"
    )

    assert post_res.status_code == 201

    with app.app_context():
        assert app_db.session.execute(app_db.select(Sandwich).where(Sandwich.name == "cheese")).fetchone() is not None
