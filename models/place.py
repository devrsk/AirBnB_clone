#!/usr/bin/python3
<<<<<<< HEAD
"""
Defines the state model
"""
from .base_model import BaseModel


class Place(BaseModel):
    """
    Blueprint for Place objects
    """
=======
""" Place Class """

from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class that inherits BaseModel """
>>>>>>> ee1e6cfa822d51f02825d116ef5105c7735fb52b
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
