#!/usr/bin/python3
"""
Unittest module for the Amenity Class.
"""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """
    Test Cases for the Amenity class.
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

    def test_8_instantiation(self):
        """
        Tests instantiation of Amenity class.
        """

        y = Amenity()
        self.assertEqual(str(type(y)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(y), BaseModel))

    def test_8_attributes(self):
        """
        Tests the attributes of Amenity class.
        """
        attributes = storage.attributes()["Amenity"]
        o = Amenity()
        for b, t in attributes.items():
            self.assertTrue(hasattr(o, b))
            self.assertEqual(type(getattr(o, b, None)), t)

if __name__ == "__main__":
    unittest.main()