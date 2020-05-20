import os
from sqlalchemy import Column, String, Integer, DateTime
from flask_sqlalchemy import SQLAlchemy
import json

# database_path set as environment variable
db = SQLAlchemy()


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('database_path')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Car(db.Model):
    __tablename__ = 'Car'

    # auto-increments, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)

    # define car attributes
    make = Column(String(80), nullable=False)
    model = Column(String(80), nullable=False)
    year = Column(Integer, nullable=False)

    def short(self):

        return {
            'id': self.id,
            'year': self.year,
            'make': self.make,
            'model': self.model
        }

    def __repr__(self):
        return json.dumps(self.short())


class Service(db.Model):
    __tablename__ = 'Service'

    # auto-increments, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)

    # define service attributes
    date = Column(DateTime, nullable=False)
    mileage = Column(Integer, nullable=False)
    notes = Column(String, nullable=False)

    cars = db.relationship("Car", backref='service')

    def short(self):
        return {
            'id': self.id,
            'date': self.date,
            'mileage': self.mileage,
            'make': self.cars.make,
            'model': self.cars.model,
            'notes': self.notes
        }

    def __repr__(self):
        return json.dumps(self.short())
