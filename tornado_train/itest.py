from tornado.web import Application, RequestHandler
from tornado.httpserver import HTTPServer
from tornado.options import define, options
from tornado.ioloop import IOLoop

define('port', default=8001, type=int)

class IRequest(RequestHandler):
	def get(self):
		name = self.get_argument('name')
		# return self.write("%s" % (name))
		self.redirect('/1/?name=11')

class HomeRequest(RequestHandler):
	def get(self, id):
		name = self.get_argument('name')
		return self.write('<h3>%s %s </h3>' % (name, id))

def main():
	app = Application(
		[(r'/([0-9]+)/', HomeRequest),
			(r'/ha/', IRequest),
		], debug=True
		)
	app.listen(options.port)
	IOLoop.instance().start()

main()