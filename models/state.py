#!/usr/bin/python3
"""
    contains state class to represent a state
"""

from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class: class to represent states of cities"""
    if (storage_engine == 'db'):
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """cities list in state
            """
            cities_list = []
            for key, value in models.storage.all(models.city.City).items():
                if (value.state_id == self.id):
                    cities_list.append(value)
            return cities_list
