#!/usr/bin/python3
'''This module will create a Review class'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''This Class is for managing review objects'''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        '''This Initializes attributes for the review class'''
        super().__init__(*args, **kwargs)
