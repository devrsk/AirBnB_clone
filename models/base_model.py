#!/usr/bin/python3
"""
Defines the base model
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes and methods for other classes
    Also links BaseModel to FileStorage by using the variable storage
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes an instance
        """
        if kwargs is not None and len(kwargs) != 0:
            if '__class__' in kwargs:
                del kwargs['__class__']
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from .__init__ import storage
            storage.new(self)

    def __str__(self):
        """
        String representation when instance is printed
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Save updates to an instance
        """
        self.__dict__.update({'updated_at': datetime.now()})
        from .__init__ import storage
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of an instance
        """
        disdict = dict(self.__dict__)
        disdict.update({'__class__': type(self).__name__,
                        'updated_at': self.updated_at.isoformat(),
                        'id': self.id,
                        'created_at': self.created_at.isoformat()})
        return disdict

""" BaseModel Class """
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ construct """

    def __init__(self, *args, **kwargs):
        """ Construct """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ String """
        return('[' + type(self).__name__ + '] (' + str(self.id) +
               ') ' + str(self.__dict__))

    def save(self):
        """ Save Function """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns dictonary"""
        aux_dict = self.__dict__.copy()
        aux_dict['__class__'] = self.__class__.__name__
        aux_dict['created_at'] = self.created_at.isoformat()
        aux_dict['updated_at'] = self.updated_at.isoformat()
        return aux_dict
