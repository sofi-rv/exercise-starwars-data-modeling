import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class FavoritesPerson(Base):
    __tablename__ = 'favoritesperson'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    person_id = Column(Integer, ForeignKey('person.id'))
    rating = Column(Integer, nullable = True) 

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(20), nullable=False)
    eyes_color = Column(String(20), nullable = True) #nullable = True es que se puede dejar vacía la información
    hair_color = Column(String(20), nullable=False)
    height = Column(Integer, nullable = False)
    age = Column(Integer, nullable = False)
    birth_year = Column(Integer, nullable = False)
    films = Column(String(250), nullable=False)
    homeworld = Column(String(50), nullable=False)
    mass = Column(Integer, nullable = True)
    skin_color = Column(String(20), nullable=False)
    created = Column(Integer, nullable = False)
    edited = Column(Integer, nullable = False)
    species = Column(String(250), nullable=False)
    starships = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    vehicles = Column(String(50), nullable=False)
    favorites_person = relationship(FavoritesPerson, backref='person', lazy=True) #backref es una autoreferencia

class FavoritesPlanets(Base):
    __tablename__ = 'favoritesplanets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    rating = Column(Integer, nullable = True) 

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    climate= Column(String(250), nullable=False)
    created =  Column(Integer, nullable = False)
    diameter = Column(Integer, nullable = False)
    edited = Column(Integer, nullable = False)
    films = Column(String(250), nullable=False)
    gravity = Column(Integer, nullable = False)
    name = Column(String(20), nullable=False)
    orbital_period = Column(Integer, nullable = False)
    population = Column(Integer, nullable = False)
    residents = Column(String(250), nullable=False)
    rotation_period= Column(Integer, nullable = False)
    surface_water = Column(Integer, nullable = False)
    terrain = Column(String(20), nullable=False)
    url = Column(String(20), nullable=False)
    favorites_planets = relationship(FavoritesPlanets, backref='planets', lazy=True) #backref es una autoreferencia

class FavoritesVehicles(Base):
    __tablename__ = 'favoritesvehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    rating = Column(Integer, nullable = True) 

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    cargo_capacity = Column(Integer, nullable = True) 
    consumables = Column(String(20), nullable=False)
    cost_in_credits = Column(Integer, nullable = True) 
    created = Column(Integer, nullable = True) 
    crew = Column(Integer, nullable = True) 
    edited = Column(Integer, nullable = True) 
    length = Column(Integer, nullable = True) 
    manufacturer = Column(String(40), nullable=False)
    max_atmosphering_speed = Column(Integer, nullable = True) 
    model = Column(String(20), nullable=False)
    name= Column(String(20), nullable=False)
    passengers = Column(Integer, nullable = True) 
    pilots = Column(String(60), nullable=False)
    films = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    vehicle_class = Column(String(20), nullable=False)
    favorites_vehicles = relationship(FavoritesVehicles, backref='vehicles', lazy=True) #backref es una autoreferencia

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    age = Column(Integer, nullable = False)
    favorites_person = relationship(FavoritesPerson, backref='user', lazy=True)
    favorites_planets = relationship(FavoritesPlanets, backref='planets', lazy=True)
    favorites_vehicles = relationship(FavoritesVehicles, backref='vehicles', lazy=True)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
