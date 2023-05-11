#!/usr/bin/python3

"""Base model that defines all common attributes/methods for other classes.
"""

import uuid
import datetime


class BaseModel:
    """Base model that defines all common attributes/methods for other classes.
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        instance_dict = self.__dict__.items()
        model_dict = {}
        for key, value in instance_dict:
            model_dict[key] = value
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
