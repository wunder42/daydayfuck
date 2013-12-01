import time, os, re
import pymongo
from django.db import models
from django.conf import settings

# Create your models here.
if 'SERVER_SOFTWARE' in os.environ:
    from bae.api import logging
    from bae.api.memcache import BaeMemcache
    from bae.core import const

    con = pymongo.Connection(host = const.MONGO_HOST, port = int(const.MONGO_PORT))
    db = con[settings.DB_NAME]
    db.authenticate(const.MONGO_USER, const.MONGO_PASS)
    cache = BaeMemcache()
else:
    import logging
    from django.core.cache import cache
    con = pymongo.Connection(host = settings.MONGO_HOST, port = int(settings.MONGO_PORT))
    db = con[settings.DB_NAME]

class Wxuser(object):

	def __init__(self, **kwargs):
		for k in kwargs.items():
			self.__dict__.update({k[0]: k[1]})

	@staticmethod
	def create_user(openid):
		user = {'openid': openid, 'jokeTimestamp': -1}
		db.t_user.save(user)
		return Wxuser(**user)

	@staticmethod 
	def update_user(openid, **kwargs):
		db.t_user.update({'openid':openid}, {'$set':kwargs})
		# return Wxuser

# user = {'openid': '123', 'create_time': int(time.time())}
# user = Wxuser(**user)
# print user.openid, user.create_time

