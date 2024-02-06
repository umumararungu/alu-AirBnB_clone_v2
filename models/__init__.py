<<<<<<< HEAD
#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
=======
"""create a unique FileStorage instance for your application"""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
<<<<<<< HEAD
    from .engine.db_storage import DBStorage

    storage = DBStorage()
    storage.reload()
else:
    from .engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
=======
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae
