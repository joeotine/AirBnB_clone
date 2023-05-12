#!/usr/bin/python3
'''This module will create a User class'''
from models.base_model import BaseModel


class User(BaseModel):
    '''This Class is for managing user objects'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        '''This Initializes attributes for the User class'''
        super().__init__(*args, **kwargs)
