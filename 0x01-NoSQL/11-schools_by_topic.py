#!/usr/bin/env python3
"""Task 11 module"""


def school_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    filter_by_topic = {
        'topics': {
            '$elemMatch': {
                    '$eq': topic,
                },
        },
    }

    return [doc for doc in mongo_collection.find(filter_by_topic)
