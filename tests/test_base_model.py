#!/usr/bin/python3

"""Test suite for the base model class
"""

import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the base model class
    """
    def test_id(self):
        """Test the id instance attribute
        """
        model1 = BaseModel()
        model2 = BaseModel()
        model1_id = model1.id
        model2_id = model2.id
        self.assertIsInstance(model1, BaseModel)
        self.assertTrue(hasattr(model1, 'id'))
        self.assertEqual(type(model1_id), str)
        self.assertNotEqual(model1_id, model2_id)

    def test_created_at(self):
        """Test the created_at instance attribute
        """
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertIsInstance(model.created_at, datetime.datetime)

    def test_updated_at(self):
        """Test the updated_at instance attribute
        """
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.updated_at, datetime.datetime)

    # def test_save(self):
    #     """Test the save instance method
    #     """
    #     model = BaseModel()
    #     self.assertIsInstance(model, BaseModel)
    #     self.assertIsInstance(model.updated_at, datetime.datetime)
    #     model.save()
    #     self.assertNotEqual(model.created_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model_dict, dict)
        self.assertIsInstance(model_dict['id'], str)
        self.assertIsInstance(model_dict['__class__'], str)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
