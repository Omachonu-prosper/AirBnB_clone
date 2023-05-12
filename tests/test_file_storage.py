#!/usr/bin/python3

"""Test the filestorage engine
"""

import unittest
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test the filestorage engine
    """
    def test_all(self):
        model = BaseModel()
        data = storage.all()
        storage_model = data.get(f"BaseModel.{model.id}")
        self.assertIsNotNone(storage_model)
        self.assertIsInstance(storage_model, BaseModel)
