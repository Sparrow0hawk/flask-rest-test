from flask import Flask, Response, render_template, request
from sqlalchemy import text

from flask_rest_test.db import add_tables
from flask_rest_test.extensions import app_db


def create_app(test_config=None) -> Flask:
    app = Flask(__name__)

    # app config
    app.config.from_object("flask_rest_test.config.Config")
    app.config.from_prefixed_env()
    if test_config:
        app.config.from_mapping(test_config)

    # extensions
    app_db.init_app(app)

    # app routes
    # TODO: refactor into blueprints
    @app.route("/")
    def index() -> str:
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

    # database data initialisation
    app_db.create_database()

    return app
