from flask import Flask
from flask_marshmallow import Marshmallow, fields
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()

#title, name, phone_number, email, sex, age, location
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    phone_number = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    sex = db.Column(db.String(1))
    age = db.Column(db.Integer)
    location = db.Column(db.String(250), nullable=False)
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, name, phone_number, email, sex, age, location):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.sex = sex
        self.age = age
        self.location = location


class UserSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    phone_number = fields.String(required=True)
    email = fields.String(required=True)
    sex = fields.String()
    age = fields.String()
    location = fields.String(required=True)
    created_date = fields.DateTime()



