#!/usr/bin/env python3
"""
Module 9-insert_school
Function to insert a new document in a MongoDB collection
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Key-value pairs representing the document fields.

    Returns:
        The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
