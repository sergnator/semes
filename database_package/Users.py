import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'example'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.Integer)
    email = sqlalchemy.Column(sqlalchemy.String)
