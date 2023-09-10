import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    diameter = Column(String(80), nullable=False)
    rotation_period = Column(String(80), nullable=False)
    orbital_period = Column(String(80), nullable=False)
    gravity = Column(String(80), nullable=False)
    population = Column(String(80), nullable=False)
    climate = Column(String(80), nullable=False)
    terrain = Column(String(80), nullable=False)
    surface_water = Column(String(80), nullable=False)

    def to_dict(self):
        return {}

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    height = Column(String(80), nullable=False)
    mass = Column(String(80), nullable=False)
    hair_color = Column(String(80), nullable=False)
    skin_color = Column(String(80), nullable=False)
    eye_color = Column(String(80), nullable=False)
    birth_year = Column(String(80), nullable=False)
    gender = Column(String(80), nullable=False)

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(40), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    def to_dict(self):
        return {}

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String(50))
    planet_name = Column(String(40), ForeignKey('planet.name'))
    person_name = Column(String(120), ForeignKey('person.name'))

    def to_dict(self):
        return {}
    
render_er(Base, 'diagram.png')
