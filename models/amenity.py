#!/usr/bin/python3
<<<<<<< HEAD
"""
Defines the state model
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Blueprint for Amenity objects
    """
=======
""" Amenity Class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits BaseModel"""
>>>>>>> ee1e6cfa822d51f02825d116ef5105c7735fb52b
    name = ""
