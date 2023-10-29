from flask import Flask, Response, render_template, request
from sqlalchemy import text

from .extensions import app_db


def create_app(test_config=None) -> Flask:
    app = Flask(__name__)

    app.config.from_object("flask_rest_test.config.Config")

    app_db.init_app(app)

    if test_config:
        app.config.from_mapping(test_config)

    @app.route("/")
    def index() -> Response:
        with app_db.engine.connect() as conn:
            res = conn.execute(text("SELECT name, count from sandwiches"))
            data = res.fetchall()

        return render_template("index.html", sandwiches=data)

    @app.route("/add", methods=["POST"])
    def add_sandwich():
        data = request.get_json()

        try:
            with app_db.engine.begin() as conn:
                conn.execute(
                    text("INSERT INTO sandwiches (name, count) VALUES (:name, :count)"),
                    {"name": data["name"], "count": data["count"]},
                )

            return Response(status=201)
        except Exception as e:
            return Response(response=f"Something went wrong: {e.__doc__}\n", status=400)

    app_db.create_database()

    return app
