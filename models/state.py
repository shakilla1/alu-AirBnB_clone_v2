#!/usr/bin/python3
"""Holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """Representation of a State"""

    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes State"""
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """Return list of City objects linked to this State (FileStorage only)"""
        if getenv('HBNB_TYPE_STORAGE') == 'db':
            return []
        all_cities = models.storage.all(City)
        return [city for city in all_cities.values() if city.state_id == self.id]
