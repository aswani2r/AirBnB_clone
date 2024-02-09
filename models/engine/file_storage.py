#!/usr/bin/python3
"""
Class definition of FileStorage.
"""
import datetime
import json
import os
from models.base_model import BaseModels

"""
serialisation and deserialisation of base model classes
"""
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets new obj in __objects with <obj class name>.id
        """
        key = f"{obj._name_.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialzes __objects to the JSON file(path:_file_path)
        """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            d = {b: t.to_dict() for b, t in FileStorage.__objects.items()}
            json.dump(d, file)

    def classes(self):
        """
        Returns a dictionary of valid classes and their references.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """
        Deserializes JSON file into __objects.
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            obj_dict = json.load(file)
            obj_dict = {b: self.classes()[t["__class__"]](**v)
                        for b, t in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def attributes(self):
        """
        Returns the valid attributes and their types for classname.
        """
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
