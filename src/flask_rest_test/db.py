from flask import current_app, g
from sqlalchemy import Engine, create_engine, String, Column, MetaData, Integer, Table


def get_db():
    if 'db' not in g:
        g.db = create_engine(current_app.config["SQLALCHEMY_DATABASE_URI"])

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.dispose()

def add_tables(metadata: MetaData) -> None:
    Table("sandwiches",
          metadata,
          Column("name", String(length=256), nullable=False, unique=True),
          Column("count", Integer)
          )

def init_app(app):
    app.teardown_appcontext(close_db)