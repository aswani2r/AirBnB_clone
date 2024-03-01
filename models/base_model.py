#!/usr/bin/python3
"""
BaseModel class definition.
Contains the Base class for the AirBnB clone console.
"""
import sys
import uuid
from datetime import datetime
import models

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
                if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self,key,value)
            
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        String representation of the BaseModel instance.
        """

        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
       Update the public instance attribute updated_at with the current datetime.
        Call save(self) method of storage.
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__ of the instance.
        """

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = my_dict["created_at"].isoformat()
        new_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return new_dict
