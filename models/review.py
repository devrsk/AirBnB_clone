#!/usr/bin/python3
<<<<<<< HEAD
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
=======
""" Review Class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits BaseModel """
    place_id = ""
    user_id = ""
>>>>>>> ee1e6cfa822d51f02825d116ef5105c7735fb52b
    text = ""
