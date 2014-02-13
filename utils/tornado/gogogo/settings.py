session = {
    "COOKIE_NAME": "asyncmongo_session",
    "DEFAULT_COOKIE_PATH": "/",
    "SESSION_EXPIRE_TIME": 7200,    # sessions are valid for 7200 seconds
                                    # (2 hours)
    "SET_COOKIE_EXPIRES": True,     # Set to True to add expiration field to
                                    # cookie
    "SESSION_TOKEN_TTL": 5,         # Number of seconds a session token is valid
                                    # for.
    "UPDATE_LAST_ACTIVITY": 60,     # Number of seconds that may pass before
                                    # last_activity is updated
    "MONGO_COLLECTION": 'sessions',
    "MONGO_COLLECTION_SIZE": 100000,
}

import tornado.options
import random
tornado.options.define("environment", default="dev", help="environment")

def randomize(values):
    """ this is a wrapper that returns a function which when called returns a random value"""
    def picker():
        return random.choice(values)
    return picker

options = {
    'dev' : {
        'mongo_database' : {'host' : '127.0.0.1', 'port' : 27017, 'dbname' : 'testdb', 'maxconnections':5}
    }
}

default = {}

def get(key):
    env = tornado.options.options.environment
    if env not in options:
        raise Exception("Invalid Environment (%s)" % env)
    v = options.get(env).get(key) or default.get(key)
    if callable(v):
        return v()
    return v

REST_DEBUG = False