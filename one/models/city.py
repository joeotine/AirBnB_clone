#!/usr/bin/python3
'''This is module that creates a User class'''
from models.base_model import BaseModel


class City(BaseModel):
    '''This Class is  for managing city objects'''
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        '''This Initializes attributes for the city class'''
        super().__init__(*args, **kwargs)
