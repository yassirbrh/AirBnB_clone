#!/usr/bin/env python3
'''
    BaseModel Class importation
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''Definition of the class City inheriting from BaseModel Class
    '''

    state_id = ""
    name = ""
