import os
from sqlalchemy import Column, String, Integer, Date
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
    id = Column(Integer, primary_key=True)

    # define car attributes
    make = Column(String(80), nullable=False)
    model = Column(String(80), nullable=False)
    year = Column(Integer, nullable=False)

    services = db.relationship("Service", backref='car')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):

        return {
            'id': self.id,
            'year': self.year,
            'make': self.make,
            'model': self.model
        }

    def __repr__(self):
        return json.dumps(self.format())


class Service(db.Model):
    __tablename__ = 'Service'

    # auto-increments, unique primary key
    id = Column(Integer, primary_key=True)

    # define service attributes
    date = Column(Date, nullable=False)
    mileage = Column(Integer, nullable=False)
    notes = Column(String, nullable=False)

    car_id = db.Column(db.Integer, db.ForeignKey('Car.id'), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):

        return {
            'id': self.id,
            'date': self.date,
            'mileage': self.mileage,
            'make': self.car.make,
            'model': self.car.model,
            'notes': self.notes
        }

    def __repr__(self):
        return json.dumps(self.format())
