#!/usr/bin/python3
<<<<<<< HEAD
"""
database storage
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """
    class properties
    """
=======
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """create tables in environmental"""
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae

    __engine = None
    __session = None

    def __init__(self):
<<<<<<< HEAD
        """Instantiation of DBStorage class"""
        MySQL_user = getenv("HBNB_MYSQL_USER")
        MySQL_pwd = getenv("HBNB_MYSQL_PWD")
        MySQL_host = getenv("HBNB_MYSQL_HOST")
        MySQL_db = getenv("HBNB_MYSQL_DB")
        MySQL_env = getenv("HBNB_ENV")
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                MySQL_user, MySQL_pwd, MySQL_host, MySQL_db
            ),
            pool_pre_ping=True,
        )
        Base.metadata.create_all(self.__engine)
        if MySQL_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Show all class objects in DBStorage or specified class if given"""
        if cls:
            objects = self.__session.query(cls).all()
        else:
            classes = [State, City, User, Place, Review, Amenity]
            objects = []
            for c in classes:
                objects += self.__session.query(c)
        my_dict = {}
        for obj in objects:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            my_dict[key] = obj
        return my_dict

    def new(self, obj):
        """Add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create the current database
        session from the engine"""
        # Base.metadata.create_all(self.__engine)  # redundant with __init__?
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes current SQLAlchemy session, discarding unsaved changes and
        updating `storage` with current state of DB.

        Project: 0x04. AirBnB clone - Web framework
        Task: 7. Improve engines
        """
=======
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, passwd, host, db),
            pool_pre_ping=True,
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return dic

    def new(self, obj):
        """add a new element in the table"""
        self.__session.add(obj)

    def save(self):
        """save changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table"""
        if obj:
            self.session.delete(obj)

    def reload(self):
        """configuration"""
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """calls remove()"""
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae
        self.__session.close()
