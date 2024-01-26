#!/usr/bin/python3
""" State Module for HBNB project """
import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from .city import City

Base = declarative_base()


class State(BaseModel, Base):
    """State class"""

    engine = create_engine("mysql://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db")

    session = sessionmaker(bind=engine)()

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", backref="state")

    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """Getter for list of all `City` objects when in file storage
            mode.
            """
            from . import storage

            cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
