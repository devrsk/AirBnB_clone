#!/usr/bin/python3
'''Base Model file'''
import uuid
import models
from datetime import datetime


class BaseModel:
    '''BaseModel Class'''
    forme = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        '''__init___'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                                                            value,
                                                            BaseModel.forme
                                                        )
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        '''Return String'''
        return ("[{}] ({}) {}".format(
                                            self.__class__.__name__,
                                            self.id,
                                            self.__dict__
                                        ))

    def save(self):
        '''Save function'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''To dictionary function'''
        new_dic = self.__dict__.copy()
        new_dic['created_at'] = self.created_at.isoformat()
        new_dic['updated_at'] = self.updated_at.isoformat()
        new_dic['__class__'] = self.__class__.__name__
        return (new_dic)
