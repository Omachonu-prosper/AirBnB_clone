#!/usr/bin/python3

"""Test that models/__init__.py exports a FileStorage instance
(storage) which should have all methods
"""

import unittest
from models import storage


class TestStorage(unittest.TestCase):
    """Test that models/__init__.py exports a FileStorage instance
    (storage) which should have all methods
    """
    def test_that_methods_exist(self):
        """Test that methods exist on storage instance
        """
        self.assertTrue(hasattr(storage, 'all'))
        self.assertTrue(hasattr(storage, 'new'))
        self.assertTrue(hasattr(storage, 'save'))
        self.assertTrue(hasattr(storage, 'reload'))
