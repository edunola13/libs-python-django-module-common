# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pymongo import MongoClient


class Setting():
    '''
        databases = Databases configurations
    '''
    databases = {
        'default': {
            'MONGO_HOST': 'localhost',
            'MONGO_PORT': 27017,
            'MONGO_DB': 'sync',
            'TZ_AWARE': False,
            'USERNAME': None,
            'PASSWORD': None,
            'AUTH_MECHANISM': 'SCRAM-SHA-256',
        }
    }
    _connections = {}

    def __init__(self):
        pass

    def load_settings(self, settings):
        for attr, value in settings.items():
            setattr(self, attr, value)

    def get_connection(self, name='default'):
        if name not in Setting._connections:
            if self.databases[name]['USERNAME']:
                mongo = MongoClient(
                    self.databases[name].get('MONGO_HOST', 'localhost'),
                    self.databases[name].get('MONGO_PORT', 27017),
                    tz_aware=self.databases[name].get('TZ_AWARE', False),
                    username=self.databases[name]['USERNAME'],
                    password=self.databases[name]['PASSWORD'],
                    authSource=self.databases[name]['MONGO_DB'],
                    authMechanism=self.databases[name]['AUTH_MECHANISM']
                )
            else:
                mongo = MongoClient(
                    self.databases[name].get('MONGO_HOST', 'localhost'),
                    self.databases[name].get('MONGO_PORT', 27017),
                    tz_aware=self.databases[name].get('TZ_AWARE', False)
                )
            Setting._connections[name] = mongo[self.databases[name]['MONGO_DB']]

        return Setting._connections[name]


settings = Setting()
