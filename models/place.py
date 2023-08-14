#!/usr/bin/env python3
'''
    Importation of the BaseModel Module
'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''Definition of the class Place inheriting from BaseModel
    '''
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
