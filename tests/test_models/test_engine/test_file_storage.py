#!/usr/bin/python3
""" Module for testing file storage"""
import unittest

import models
from models.base_model import BaseModel
import os


<<<<<<< HEAD
class test_fileStorage(unittest.TestCase):
    """Class to test the file storage method"""

    def setUp(self):
        """Set up test environment"""
=======
@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "skip if not db")
class TestFileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        self.storage = models.storage
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae
        del_list = []
        for key in self.storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del self.storage._FileStorage__objects[key]

    def tearDown(self):
        """Remove storage file at end of tests"""
        try:
            os.remove("file.json")
        except:
            pass

        del self.storage

    def test_obj_list_empty(self):
<<<<<<< HEAD
        """__objects is initially empty"""
        self.assertEqual(len(storage.all()), 0)
=======
        """ __objects is initially empty """
        self.assertEqual(len(self.storage.all()), 0)
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae

    def test_new(self):
        """New object is correctly added to __objects"""
        new = BaseModel()
        for obj in self.storage.all().values():
            temp = obj
            self.assertTrue(temp is obj)

    def test_all(self):
        """__objects is properly returned"""
        new = BaseModel()
        temp = self.storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """File is not created on BaseModel save"""
        new = BaseModel()
        self.assertFalse(os.path.exists("file.json"))

    def test_empty(self):
        """Data is saved to file"""
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize("file.json"), 0)

    def test_save(self):
        """FileStorage save method"""
        new = BaseModel()
<<<<<<< HEAD
        storage.save()
        self.assertTrue(os.path.exists("file.json"))
=======
        self.storage.save()
        self.assertTrue(os.path.exists('file.json'))
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae

    def test_reload(self):
        """Storage file is successfully loaded to __objects"""
        new = BaseModel()
        self.storage.save()
        self.storage.reload()
        for obj in self.storage.all().values():
            loaded = obj
<<<<<<< HEAD
        self.assertEqual(new.to_dict()["id"], loaded.to_dict()["id"])
=======
            self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae

    def test_reload_empty(self):
        """Load from an empty file"""
        with open("file.json", "w") as f:
            pass
        with self.assertRaises(ValueError):
            self.storage.reload()

    def test_reload_from_nonexistent(self):
<<<<<<< HEAD
        """Nothing happens if file does not exist"""
        self.assertEqual(storage.reload(), None)
=======
        """ Nothing happens if file does not exist """
        self.assertEqual(self.storage.reload(), None)
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae

    def test_base_model_save(self):
        """BaseModel save method calls storage save"""
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_type_path(self):
<<<<<<< HEAD
        """Confirm __file_path is string"""
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """Confirm __objects is a dict"""
        self.assertEqual(type(storage.all()), dict)
=======
        """ Confirm __file_path is string """
        self.assertEqual(type(self.storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(self.storage.all()), dict)
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae

    def test_key_format(self):
        """Key is properly formatted"""
        new = BaseModel()
<<<<<<< HEAD
        _id = new.to_dict()["id"]
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, "BaseModel" + "." + _id)
=======
        _id = new.to_dict()['id']
        for key in self.storage.all().keys():
            temp = key
            self.assertEqual(temp, 'BaseModel' + '.' + _id)
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae

    def test_storage_var_created(self):
        """FileStorage object storage created"""
        from models.engine.file_storage import FileStorage
<<<<<<< HEAD

        print(type(storage))
        self.assertEqual(type(storage), FileStorage)
=======
        print(type(self.storage))
        self.assertEqual(type(self.storage), FileStorage)
>>>>>>> cf3b2eaad5de06728128fd52190d0756905e95ae
