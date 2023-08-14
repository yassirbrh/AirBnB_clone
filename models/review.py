#!/usr/bin/env python3
'''
    Importation of the BaseModel Module
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Definition of the class Review inheriting from BaseModel
    '''
    place_id = ""
    user_id = ""
    text = ""
