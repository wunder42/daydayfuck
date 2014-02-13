import tornado.ioloop
import pyrestful.rest

from pyrestful import mediatypes
from pyrestful.rest import get, post, put, delete

class TodoResource(pyrestful.rest.RestHandler):

	def initialize(self, database=None):
		self.databse = database

	@get(_path='/v1/todo/{id}', _types=[int], _produces=mediatypes.APPLICATION_JSON)
	def getTodo(self, id):
		''''''
		return self.write('123')

if __name__ == '__main__':

	app = pyrestful.rest.RestService([TodoResource], {})
	app.listen(8989)
	tornado.ioloop.IOLoop.instance().start()





