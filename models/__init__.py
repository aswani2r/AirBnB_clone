#!/usr/bin/python3
"""
Module for FileStorage autoinitialization.
"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
