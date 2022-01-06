import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    Password = Column(String(50), nullable=False)

class People(Base):
    __tablename__ = 'People'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    gender = Column(String(250))
    homeworld = Column(String(250))
    films = Column(String(250))
    species = Column(String(250))
    vehicles = Column(String(250))
    starships = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    url = Column(String(250))
    
    def to_dict(self):
        return {}

class Planet(Base):
    __tablename__ = 'Planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(250))
    population = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer)
    created = Column(String(250))
    edited = Column(String(250))
    url = Column(String(250))


    def to_dict(self):
        return {}

class Vehicle(Base):
    __tablename__ = 'Vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    model = Column(String(250))
    vehicle_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(250))
    films = Column(String(250))
    pilots = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    url = Column(String(250))

    def to_dict(self):
        return {}   

# --------------  Tablas Pivote  -------------------------------------

class Favorite_People(Base):
    __tablename__ = 'Favorite_People'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    people_id = Column(Integer, ForeignKey('People.id'))

    user = relationship(User)
    people = relationship(People)

    def to_dict(self):
        return {}   

class Favorite_People(Base):
    __tablename__ = 'Favorite_Planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    planet_id = Column(Integer, ForeignKey('Planet.id'))

    user = relationship(User)
    planet = relationship(Planet)

    def to_dict(self):
        return {}   

class Favorite_Vehicle(Base):
    __tablename__ = 'Favorite_Vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    vehicle_id = Column(Integer, ForeignKey('Vehicle.id'))

    user = relationship(User)
    vehicle = relationship(Vehicle)

    def to_dict(self):
        return {}    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')