#!/usr/bin/python3
<<<<<<< HEAD
"""
Class User that inherits from BaseModel
"""

=======
""" User Class """
>>>>>>> ee1e6cfa822d51f02825d116ef5105c7735fb52b
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """
    Blueprint for a User object
    Public Attributes that will use FileStorage in engine
    folder to manage serialization and deserialization of User
    """
=======
    """ User class that inherits BaseModel """
>>>>>>> ee1e6cfa822d51f02825d116ef5105c7735fb52b
    email = ""
    password = ""
    first_name = ""
    last_name = ""
