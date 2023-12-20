#!/usr/bin/env python3
"""Task 0 module"""
import uuid
import redis


class Cache():
    """A cache class"""
    def __init__(self):
       self._redis = redis.Redis()
       self._redis.flushdb()

    def store(self, data) -> str:
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
