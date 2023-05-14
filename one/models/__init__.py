#!/usr/bin/python3
"""This initializes the package for the models directory"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
