from flask import Flask
from marshmallow import Schema, fields,pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()


class Collage(db.Model):
    __tablename__ = 'collages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self,name):
        self.name = name

class CollageSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)


class Biodata(db.Model):
    __tabelname__ = 'biodatas'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nim = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    collage_id = db.Column(db.Integer, db.ForeignKey('collages.id',ondelete='CASCADE'),nullable=False)
    collage = db.relationship('Collage', backref=db.backref('biodatas',lazy='dynamic'))

    def __init__(self,nim,name,collage_id):
        self.nim = nim
        self.name = name
        self.collage_id = collage_id


class BiodataSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    collage_id = fields.Integer(required=True)
    nim = fields.Integer(required=True)
    name = fields.String(required=True, validate=validate.Length(1))









