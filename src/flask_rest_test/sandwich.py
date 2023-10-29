from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from flask_rest_test.db import app_db


class Sandwich(app_db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=256), nullable=False, unique=True)
    count: Mapped[int] = mapped_column(Integer)
