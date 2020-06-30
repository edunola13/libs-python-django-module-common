=====
Module Common
=====

Module Common is a Django app for common functionallities.

Quick start
-----------

1. Add the next optional settings fro Mongo:
    settings_mongo.load_settings({
	    'databases': {
	        'default': {
	            'MONGO_HOST': 'localhost',
	            'MONGO_PORT': 9999,
	            'MONGO_DB': 'name_db',
	            'TZ_AWARE': True,
	            'USERNAME': 'eduardo_n',
	            'PASSWORD': 'eduardo_n',
	            'AUTH_MECHANISM': 'SCRAM-SHA-256',
	        }
	    }
	})
	MONGO_CONFIG = settings_mongo

	Username, Password y Auth Mechanism are optional.
