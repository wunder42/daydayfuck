import os, sys, logging, pymongo

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from tornado.options import define, parse_command_line, options
from handlers.handler import Login, Register, Logout, Home, EchoHandler, NewHome, ChatHandler

import settings


class IApplication(Application):

	def __init__(self):

		handlers = [
			(r'/', Home),
			(r'/login', Login),
			(r'/logout', Logout),
			(r'/register', Register),

			(r'/message', EchoHandler),
			(r'/home', NewHome),
			(r'/chat/c', ChatHandler),
		]

		settings = {
			'cookie_secret': 'tfdsaljfdsalgtel',
			'xsrc_cookies': True,
			'login_url': '/login', 
			'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
			'static_path': os.path.join(os.path.dirname(__file__), 'public'),
			'debug': True
		}
		
		super(IApplication, self).__init__(handlers, **settings)
		self.db = pymongo.Connection(settings.DB_HOST, settings.DB_PORT)[settings.DB_NAME]

define('port', default=8989, type=int)

sys.path.append('./settings.py')

parse_command_line()
app = IApplication()
app.listen(options.port)
IOLoop.instance().start()