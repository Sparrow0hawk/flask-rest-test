from flask import Flask, Response, render_template, request, make_response
from sqlalchemy import MetaData, create_engine, text

from .db import add_tables, get_db

def create_app() -> Flask:
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    @app.route("/")
    def index() -> Response:

        db = get_db()

        with db.connect() as conn:
            res = conn.execute(text("SELECT name, count from sandwiches"))
            data = res.fetchall()

        return render_template("index.html", sandwiches = data)

    @app.route("/add", methods=["POST"])
    def add_sandwich():
        db = get_db()
        data = request.get_json()

        try:
            with db.begin() as conn:
                conn.execute(text("INSERT INTO sandwiches (name, count) VALUES (:name, :count)"),
                                      {"name": data["name"], "count": data["count"]})

            return Response(status=201)
        except Exception as e:
            return Response(response=f"Something went wrong: {e.__doc__}\n", status=400)

    from . import db
    db.init_app(app)
    _create_database(app.config["SQLALCHEMY_DATABASE_URI"])

    return app


def _create_database(database_uri: str) -> None:
    metadata = MetaData()
    add_tables(metadata)

    engine = create_engine(database_uri, echo=True)

    metadata.create_all(engine)