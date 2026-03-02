#!/usr/bin/python3
"""State Module for HBNB project"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        # DBStorage: define relationship
        cities = relationship(
            'City',
            backref="state",
            cascade="all, delete, delete-orphan"
        )

    @property
    def cities(self):
        """
        FileStorage: return list of City instances with state_id equal to
        the current State.id
        """
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            return []  # DBStorage uses relationship
        city_list = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
