#! /usr/bin/python

import redis
# print redis.__file__

r = redis.Redis(host='127.0.0.1', port=6379, db=1)

# r.set('name', 'zeizei')
# r['name'] = 'knife'
print r.keys(), r.get('name'), r.dbsize()