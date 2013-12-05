import pymongo
import settings

class Mongo(Object):

	def __init__(self):
		if hasattr(self, 'single'): return self.__getattr__('single')
		self.db = pymongo.Connection(settings.DB_HOST, settings.DB_PORT)
		self.__setattr__('single', Mongo())
		
	def insert(table, obj):
		self.db.[table].insert(obj)