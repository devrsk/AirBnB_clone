#!/usr/bin/python3
<<<<<<< HEAD
"""
Create a unique FileStorage instance for your application
"""
from .engine.file_storage import FileStorage


=======
""" initialization for class FileStorage """
from models.engine.file_storage import FileStorage
>>>>>>> ee1e6cfa822d51f02825d116ef5105c7735fb52b
storage = FileStorage()
storage.reload()
