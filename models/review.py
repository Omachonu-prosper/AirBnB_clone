#!/usr/bin/python3

"""Exports the Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review inherits from BaseModel
    """
    user_id = ''
    place_id = ''
    test = ''
