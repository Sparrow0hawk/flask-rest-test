from flask import Flask
from sqlalchemy import Column, Engine, Integer, MetaData, String, Table, create_engine


class Database:
    def __init__(self, app: Flask | None = None):
        self.engine: Engine

        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        self.engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], echo=True)

        app.extensions["database"] = self

    def create_database(self) -> None:
        metadata = MetaData()
        add_tables(metadata)

        metadata.create_all(self.engine)


def add_tables(metadata: MetaData) -> None:
    Table(
        "sandwiches",
        metadata,
        Column("name", String(length=256), nullable=False, unique=True),
        Column("count", Integer),
    )
