#!/usr/bin/python3
"""This is the state class"""
import os
from models import storage
from base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import shlex
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = (
        relationship("City", cascade="all, delete, delete-orphan", backref="state")
        if os.getenv("HBNB_TYPE_STORAGE") == "db"
        else ""
    )

    @property
    def cities(self):
        var = storage.all()
        lista = []
        result = []
        for key in var:
            city = key.replace(".", " ")
            city = shlex.split(city)
            if city[0] == "City":
                lista.append(var[key])
        for elem in lista:
            if elem.state_id == self.id:
                result.append(elem)
        return result


engine = create_engine("mysql+mysqldb://hbnb_dev:hbnb_dev_pwd/hbnb_dev_db@localhost")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
