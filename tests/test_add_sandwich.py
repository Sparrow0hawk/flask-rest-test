import json

from flask import Flask
from flask.testing import FlaskClient
from sqlalchemy import text

from flask_rest_test.db import get_db

def test_add_sandwich_adds_sandwich(client: FlaskClient, app: Flask):
    with app.app_context():
        with get_db().begin() as conn:
            conn.execute(text("DELETE from sandwiches"))

    post_res = client.post("/add", data=json.dumps({"name":"cheese", "count":"10"}), content_type='application/json')

    assert post_res.status_code == 201

    with app.app_context():
        with get_db().connect() as conn:
            assert conn.execute(text("SELECT * FROM sandwiches WHERE name = 'cheese'")).fetchone() is not None
