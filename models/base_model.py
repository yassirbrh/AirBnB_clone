#!/usr/bin/env python3
'''
    IMPORT UUID, DATETIME
'''

import uuid
from datetime import datetime
import models

'''
    Creation of the class BaseModel
'''


class BaseModel:
    '''
        Definition of the class BaseModel
    '''

    def __init__(self, *args, **kwargs):
        '''
            Initialisation of the instance of class
        '''
        if len(kwargs) != 0:
            for key in kwargs:
                if key == 'created_at' or key == 'updated_at':
                    str_format = "%Y-%m-%dT%H:%M:%S.%f"
                    time_obj = datetime.strptime(kwargs[key], str_format)
                    setattr(self, key, time_obj)
                elif key != '__class__':
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        '''
            print the object in string format
        '''
        output = "[" + str(self.__class__.__name__) + "] (" + str(self.id)
        output += ") " + str(self.__dict__)
        return output

    def save(self):
        '''
            save - Function
            Updates the updated_at with the current time
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
            to_dict - Function
            returns a dictionary containing all keys/values of
            __dict__ of the instance
        '''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat("T")
        obj_dict['updated_at'] = self.updated_at.isoformat("T")
        return obj_dict
