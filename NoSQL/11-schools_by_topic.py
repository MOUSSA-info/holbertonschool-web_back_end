#!/usr/bin/env python3
"""
Module 11-schools_by_topic
Contains the function schools_by_topic that returns all schools having a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of school documents that have the specified topic.

    Args:
        mongo_collection: A pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        List of documents where 'topics' field contains the given topic.
        Returns an empty list if no documents found or if 'topics' field is absent.
    """
    return list(mongo_collection.find({"topics": topic}))
