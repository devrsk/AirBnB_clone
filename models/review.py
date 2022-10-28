#!/usr/bin/python3
"""
Defines the state model
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Blueprint for Review objects
    """
    user_id = ""
    place_id = ""

""" Review Class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits BaseModel """
    place_id = ""
    user_id = ""
    text = ""
