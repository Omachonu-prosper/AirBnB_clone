#!/usr/bin/python3

"""Serializes instances to a JSON file and deserializes
JSON file to instances
"""

import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """Serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the class attribute dictionary __objects
        """
        return self.__objects

    def show(self, id):
        """Return the instance with the id if found
        Return none if id is not found
        """
        return self.__objects.get(id)

    def destroy(self, obj):
        """Delete an instamce of an object from storage
        """
        del self.__objects[f"{obj.__class__.__name__}.{obj.id}"]
        self.save()

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)
        """
        objects = {}
        for key, value in self.__objects.items():
            objects[key] = value.to_dict()

        with open(self.__file_path, 'w+') as f:
            json.dump(objects, f)

    def reload(self):
        """Seserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        objects = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)

            for key, value in objects.items():
                self.__objects[key] = eval(f"{value['__class__']}(**{value})")
