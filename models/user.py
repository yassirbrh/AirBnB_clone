#!/usr/bin/env python3
'''
    BaseModel Class importation
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Definition of the class User inheriting from BaseModel Class
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
