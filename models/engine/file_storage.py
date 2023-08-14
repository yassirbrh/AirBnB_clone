#!/usr/bin/env python3
'''
    Modules importation
'''
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    '''
    Creation of the class FileStorage
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
            all - instance method
            Returns the objects in the __objects array
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
            new - instance method
            Add the new object to the __objects array
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''
            save - instance method
            serializes __objects to the JSON file (path: __file_path)
        '''
        filename = FileStorage.__file_path
        objects = {}
        for key in FileStorage.__objects.keys():
            objects[key] = FileStorage.__objects[key].to_dict()
        with open(filename, "w+") as fp:
            json.dump(objects, fp)

    def reload(self):
        '''
            reload - instance method
            deserializes the JSON file to __objects
        '''
        filename = FileStorage.__file_path
        if not os.path.exists(filename):
            return
        with open(filename, "r+") as fp:
            inst_dict = json.load(fp)
            for obj_dict in inst_dict.values():
                cls_name = obj_dict['__class__']
                del obj_dict['__class__']
                cls_init = globals()[cls_name]
                new_obj = cls_init(**obj_dict)
                self.new(new_obj)
