from flask_sqlalchemy import SQLAlchemy
from app import db

# Utente base
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    user_type = db.Column(db.String(20), nullable=False)

# Aeroporto
class Airport(db.Model):
    __tablename__ = 'airports'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)

# Tratta tra due aeroporti
class Route(db.Model):
    __tablename__ = 'routes'
    id = db.Column(db.Integer, primary_key=True)
    departure_id = db.Column(db.Integer, db.ForeignKey('airports.id'))
    arrival_id = db.Column(db.Integer, db.ForeignKey('airports.id'))

    departure = db.relationship("Airport", foreign_keys=[departure_id])
    arrival = db.relationship("Airport", foreign_keys=[arrival_id])

# Volo specifico su una tratta
class Flight(db.Model):
    __tablename__ = 'flights'
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('routes.id'))
    company_id = db.Column(db.Integer, db.ForeignKey('users.id')) 
    date = db.Column(db.DateTime, nullable=False)
    seats_total = db.Column(db.Integer, nullable=False)
    seats_available = db.Column(db.Integer, nullable=False)

    price_economy = db.Column(db.Float)
    price_business = db.Column(db.Float)
    price_first = db.Column(db.Float)

    route = db.relationship('Route')
    company = db.relationship('User')

# Biglietto
class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    passenger_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.id'))
    seat_class = db.Column(db.String(20))
    extras = db.Column(db.String(200))
    seat_number = db.Column(db.String(5))

    passenger = db.relationship('User')
    flight = db.relationship('Flight')
