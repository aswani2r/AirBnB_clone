#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import time
from models.user import User
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    """Test Cases for the User class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of User class."""

        o = User()
        self.assertEqual(str(type(o)), "<class 'models.user.User'>")
        self.assertIsInstance(o, User)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of User class."""
        attributes = storage.attributes()["User"]
        o = User()
        for b, t in attributes.items():
            self.assertTrue(hasattr(o, b))
            self.assertEqual(type(getattr(o, b, None)), t)

if __name__ == "__main__":
    unittest.main()
