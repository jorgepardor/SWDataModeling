import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False, unique=True)
    user_password = Column(String(32), nullable=False)
    user_avatar = Column(String(64))

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    ship_id = Column(Integer, ForeignKey('starships.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    char_id = Column(Integer, ForeignKey('characters.id'))

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(72), nullable=False)
    gender_id = Column(Integer, ForeignKey('gender_select.id'))
    image = Column(String(250))
    height = Column(Float)
    mass = Column(Integer)
    hair_color = Column(Integer, ForeignKey('color_select.id'))
    skin_color = Column(Integer, ForeignKey('color_select.id'))
    eye_color = Column(Integer, ForeignKey('color_select.id'))
    birht_year = Column(Integer)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(72), nullable=False, unique=True)
    image = Column(String(250))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(Integer)
    population = Column(Integer)
    climate_id = Column(Integer, ForeignKey('climate_select.id'))
    terrain_id = Column(Integer, ForeignKey('terrain_select.id') )
    surface_water = Column(Integer)

class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(72), nullable=False, unique=True)
    image = Column(String(250))
    starship_class = Column(Integer, ForeignKey('ship_class_select.id'))
    manufacturer = Column(Integer, ForeignKey('ship_maker_select.id'))
    cost_in_credits = Column(Integer)
    lenght = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmopheric_speed = Column(Integer)
    hyperdrive_rating = Column(Integer)
    mglt = Column(Integer)
    cargo_capacity = Column(Integer)
    consumable = Column(Integer)

class Homeworld(Base):
    __tablename__ = 'homeworld'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_id = Column(String(72), ForeignKey('planets.id'), nullable=False)
    char_id = Column(String(72), ForeignKey('characters.id'), nullable=False)

class Pilots(Base):
    __tablename__ = 'pilots'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    starships_id = Column(String(72), ForeignKey('starships.id'), nullable=False)
    char_id = Column(String(72), ForeignKey('characters.id'), nullable=False)

class ClimateSelect(Base):
    __tablename__ = 'climate_select'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(72), nullable=False, unique=True)

class TerrainSelect(Base):
    __tablename__ = 'terrain_select'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(72), nullable=False, unique=True)

class GenderSelect(Base):
    __tablename__ = 'gender_select'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(72), nullable=False, unique=True)

class ColorSelect(Base):
    __tablename__ = 'color_select'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    color_name = Column(String(72), nullable=False, unique=True)
    color_value = (String(72))

class ShipClassSelect(Base):
    __tablename__ = 'ship_class_select'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(72), nullable=False, unique=True)

class ShipMakerSelect(Base):
    __tablename__ = 'ship_maker_select'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(72), nullable=False, unique=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')