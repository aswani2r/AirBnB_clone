#!usr/bin/python3
"""
base class for basemodels contained here.
"""
import uuid
import sys
from datetime import datetime
import models

class BaseModel:
    def __init__(self,*args, **kwargs):
        if kwargs:
            for kkey, value in kwargs.item():
                if key =="created_at" or key == "updated_at":
                    setattr(self, key, datetime.striptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now().isoformat()
        models.storage.save()

    def to_dict(self):
        dict_repr = self.__dict__.copy()}
        dict_rep['__class__'] = type(self).__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return obj_dict
