#!/usr/bin/env python3
'''
    Importation of the BaseModel Module
'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Definition of the class Amenity inheriting from BaseModel
    '''
    name = ""
