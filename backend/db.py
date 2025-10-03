from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


class Base(DeclarativeBase, MappedAsDataclass):
    @classmethod
    def new(cls, **kwargs):
        return cls(id=None, **kwargs)


db = SQLAlchemy(model_class=Base)
