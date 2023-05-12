#!/usr/bin/python3
'''This module will create a User class'''
from models.base_model import BaseModel


class State(BaseModel):
    '''This Class is for managing state objects'''
    name = ""

    def __init__(self, *args, **kwargs):
        '''This Initializes attributes for the State class'''
        super().__init__(*args, **kwargs)
