#!/usr/bin/python3
"""
Unittest module for the Place Class.
"""

import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    """
    Test Cases for the Place class.
    """

    def setUp(self):
        """
        Sets up  the test methods.
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
        Resets the FileStorage data.
        """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """
        Tests instantiation of Place class.
        """

        y = Place()
        self.assertEqual(str(type(y)), "<class 'models.place.Place'>")
        self.assertIsInstance(y, Place)
        self.assertTrue(issubclass(type(y), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Place class."""
        attributes = storage.attributes()["Place"]
        o = Place()
        for b, t in attributes.items():
            self.assertTrue(hasattr(o, b))
            self.assertEqual(type(getattr(o, b, None)), t)

if __name__ == "__main__":
    unittest.main()
