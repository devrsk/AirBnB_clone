#!/usr/bin/python3
<<<<<<< HEAD
"""
Defines the state model
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    Blueprint for City objects
    """
=======
""" City Class """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class that inherits BaseModel """
>>>>>>> ee1e6cfa822d51f02825d116ef5105c7735fb52b
    state_id = ""
    name = ""
