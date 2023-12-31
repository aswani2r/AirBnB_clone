#!/usr/bin/python3
"""
Unittest module for the BaseModel Class.
"""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import unittest
import uuid
import json
import os
import re
import time

class TestBaseModel(unittest.TestCase):

    """
    Test Cases for the BaseModel class.
    """

    def setUp(self):
        """
        Sets up test methods.
        """
        pass

    def tearDown(self):
        """
        Tears down test methods.
        """
        self.resetStorage()
        pass

    def resetStorage(self):
        """
        Resets FileStorage data.
        """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_3_instantiation(self):
        """
        Tests instantiation of BaseModel class.
        """

        y = BaseModel()
        self.assertEqual(str(type(y)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(y, BaseModel)
        self.assertTrue(issubclass(type(y), BaseModel))

    def test_3_init_no_args(self):
        """
        Tests __init__ with no arguments.
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing one required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_3_init_many_args(self):
        """
        Tests __init__ with many arguments.
        """
        self.resetStorage()
        args = [i for i in range(1000)]
        y = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        y = BaseModel(*args)

    def test_3_attributes(self):
        """
        Tests attributes value for instance of a BaseModel class.
        """

        attributes = storage.attributes()["BaseModel"]
        o = BaseModel()
        for b, t in attributes.items():
            self.assertTrue(hasattr(o, t))
            self.assertEqual(type(getattr(o, b, None)), t)

    def test_3_datetime_created(self):
        """
        Tests if updated_at & created_at are current at creation.
        """
        date_now = datetime.now()
        y = BaseModel()
        diff = y.updated_at - y.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = y.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_3_id(self):
        """
        Tests for unique user ids.
        """

        l = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(l)), len(l))

    def test_3_save(self):
        """
        Tests the public instance method save().
        """

        y = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        y.save()
        diff = y.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_3_str(self):
        """
        Tests for __str__ method.
        """
        y = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(y))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), y.id)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        d2 = y.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)

    def test_3_to_dict(self):
        """
        Tests the public instance method to_dict().
        """

        y = BaseModel()
        y.name = "Darlin"
        y.age = 21
        d = y.to_dict()
        self.assertEqual(d["id"], y.id)
        self.assertEqual(d["__class__"], type(y).__name__)
        self.assertEqual(d["created_at"], y.created_at.isoformat())
        self.assertEqual(d["updated_at"], y.updated_at.isoformat())
        self.assertEqual(d["name"], y.name)
        self.assertEqual(d["age"], y.age)

    def test_3_to_dict_no_args(self):
        """
        Tests to_dict() with no arguments.
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        msg = "to_dict() missing one required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_3_to_dict_excess_args(self):
        """
        Tests to_dict() with too many arguments.
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, 98)
        msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_4_instantiation(self):
        """
        Tests instantiation with **kwargs.
        """

        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

    def test_4_instantiation_dict(self):
        """
        Tests instantiation with **kwargs from custom dict.
        """
        d = {"__class__": "BaseModel",
             "updated_at":
             datetime(2050, 12, 30, 23, 59, 59, 123456).isoformat(),
             "created_at": datetime.now().isoformat(),
             "id": uuid.uuid4(),
             "var": "foobar",
             "int": 108,
             "float": 3.14}
        o = BaseModel(**d)
        self.assertEqual(o.to_dict(), d)

    def test_5_save(self):
        """
        Tests that storage.save() is called from save().
        """
        self.resetStorage()
        y = BaseModel()
        y.save()
        key = "{}.{}".format(type(y).__name__, y.id)
        d = {key: y.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as file:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            file.seek(0)
            self.assertEqual(json.load(file), d)

    def test_5_save_no_args(self):
        """
        Tests save() with no arguments.
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        msg = "save() missing one required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_save_excess_args(self):
        """
        Tests save() with too many arguments.
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        msg = "save() takes one positional argument but two were given"
        self.assertEqual(str(e.exception), msg)

if __name__ == '__main__':
    unittest.main()
