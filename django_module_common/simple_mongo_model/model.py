# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bson import ObjectId

from django_module_common.simple_mongo_model import settings


class ModelBase(dict):
    """
    A simple model that wraps mongodb document
    """
    __getattr__ = dict.get
    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

    _collection_name = 'default'  # Override
    _connection = 'default'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    @classmethod
    def get_collection(cls):
        return settings.get_connection(
            cls._connection
        )[cls._collection_name]

    @classmethod
    def get_object(cls, id):
        instance = cls()
        instance._id = id
        instance.reload()
        return instance

    @classmethod
    def map_objects(cls, query):
        return list(map(cls, query))

    @classmethod
    def next_object(cls, query):
        data = query.next()
        return cls(data)

    def save(self):
        if not self._id:
            self.get_collection().insert(self)
        else:
            self.get_collection().update(
                {"_id": ObjectId(self._id)}, self)

    def reload(self):
        if self._id:
            self.update(self.get_collection().find_one({"_id": ObjectId(self._id)}))

    def remove(self):
        if self._id:
            self.get_collection().remove({"_id": ObjectId(self._id)})
            self.clear()


# Example
# class ModelX(ModelBase):
#     _collection_name = 'changes_log'
