#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
<<<<<<< HEAD
    """This class manages storage of hbnb models in JSON format"""
=======
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
<<<<<<< HEAD
        """Returns a dictionary of models currently in storage, or all of
        one type.

        Args:
            cls (BaseModel-derived): class of object to list

        Returns:
            all_of_class (dict): dictionary of all objects in file storage
                of class `cls`.
        """
        if cls is None:
            return self.__objects
        else:
            all_of_class = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    all_of_class[key] = value
            return all_of_class

    def new(self, obj):
        """Adds new object to storage dictionary"""
        # self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, "w") as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, "r") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)
=======
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace(".", " ")
                partition = shlex.split(partition)
                if partition[0] == cls.__name__:
                    dic[key] = self.__objects[key]
            return dic
        else:
            return self.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path"""
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
<<<<<<< HEAD
        """delete an object if it exists"""
        try:
            if obj:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                del self.__objects[key]
        except:
            pass

    def close(self):
        """File storage equivalent to `DBStorage.close()`, resets current
        `storage` by reloading JSON file.

        Project: 0x04. AirBnB clone - Web framework
        Task: 7. Improve engines
        """
=======
        """delete an existing element"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """calls reload()"""
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae
        self.reload()
