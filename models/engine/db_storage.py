#!/usr/bin/python3
"""
Contains the class DBStorage
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity

classes = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class DBStorage:
    """Interacts with the MySQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{pwd}@{host}/{db}",
            pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)
        self.reload()

    def all(self, cls=None):
        """Query all objects"""
        new_dict = {}
        for clss in classes.values():
            if cls is None or cls == clss or cls == clss.__name__:
                objs = self.__session.query(clss).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Add object to current session"""
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """Commit changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from current session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and initialize session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        self.__session = scoped_session(session_factory)

    def close(self):
        """Remove the current session and create a fresh one"""
        self.__session.remove()
        self.reload()
