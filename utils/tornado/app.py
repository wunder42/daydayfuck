import os, pymongo

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from tornado.options import default, parse_command_line, options



class IApplication(Application):

	def __init__(self):
		handlers = [
			r('/',)
		]
		settings = {
			'cookie_secret': 'tfdsaljfdsalgtel',
			'xsrc_cookies': True,
			'login_url': '/login', 
			'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
			'debug': True
		}

		super(IApplication, self).__init__(handlers, **settings)

options('port', default=8989, type=int)

parse_command_line()
app = IApplication()
app.listen(options.port)
IOLoop.instance().start()