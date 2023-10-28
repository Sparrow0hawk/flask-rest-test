from flask.testing import FlaskClient


def test_index(client: FlaskClient):
    res = client.get("/")

    assert "<h1>The Big Sandwich Shop</h1>" in res.text
