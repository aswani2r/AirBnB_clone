#!/usr/bin/python3
"""
BaseModel class definition.
Contains the Base class for the AirBnB clone console.
"""
import sys
import uuid
from datetime import datetime

class BaseModel:

    """
    Constructor method to initialize BaseModel instance.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializing of a Base instance.
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
            
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
       Update the public instance attribute updated_at with the current datetime.
        Call save(self) method of storage.
        """
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__ of the instance.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
