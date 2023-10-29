from flask import Flask, Response, render_template, request

from flask_rest_test.db import app_db
from flask_rest_test.sandwich import Sandwich


def create_app(test_config=None) -> Flask:
    app = Flask(__name__)

    # app config
    app.config.from_object("flask_rest_test.config.Config")
    app.config.from_prefixed_env()
    if test_config:
        app.config.from_mapping(test_config)

    # extensions
    app_db.init_app(app)

    # database data initialisation
    with app.app_context():
        app_db.create_all()

    # app routes
    # TODO: refactor into blueprints
    @app.route("/")
    def index() -> str:
        data = app_db.session.execute(app_db.select(Sandwich)).scalars()
        return render_template("index.html", sandwiches=data)

    @app.route("/add", methods=["POST"])
    def add_sandwich():
        data = request.get_json()
        try:
            sandwich = Sandwich(id=data["id"], name=data["name"], count=int(data["count"]))
            app_db.session.add(sandwich)
            app_db.session.commit()
            return Response(status=201)
        except Exception as e:
            return Response(response=f"Something went wrong: {e.__doc__}\n", status=400)

    return app
