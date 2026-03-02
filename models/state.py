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

    # DBStorage: define relationship only if DB
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City',
            backref="state",
            cascade="all, delete, delete-orphan"
        )

    # FS mode: always define property, even in DB mode
    @property
    def cities(self):
        """
        Returns list of City instances linked to the State.
        Works for FileStorage engine.
        """
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # In DB, the relationship handles cities
            return self.__dict__.get('cities', [])
        # FileStorage: return filtered list
        return [c for c in models.storage.all(City).values()
                if c.state_id == self.id]
