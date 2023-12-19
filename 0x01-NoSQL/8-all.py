#!/usr/bin/env python3
"""Task 8 module"""


def list_all(mongo_collection):
    """deletes all documents with name="Holberton school"""
    return [doc for doc in mongo_collection.find()]
