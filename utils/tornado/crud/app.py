import os

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.options import define, parse_command_line, options
import motorengine.connection

from handlers import IndexHandler, TestHandler, AddHandler, DeleteHandler, UpdateHandler
import settings

class Application(Application):

	def __init__(self):

		handlers = [
			(r'/', IndexHandler),
			(r'/test', TestHandler),
			(r'/add', AddHandler),
			(r'/delete', DeleteHandler),
			(r'/update', UpdateHandler),
		]

		settings = {
			'cookie_secret': 'tfdsaljfdsalgtel',
			'xsrc_cookies': True,
			'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
			'static_path': os.path.join(os.path.dirname(__file__), 'static'),
			'debug': True
		}
		
		super(Application, self).__init__(handlers, **settings)



define('port', default=8989, type=int)
parse_command_line()
app = Application()
app.listen(options.port)
io_loop = IOLoop.instance()
motorengine.connection.connect(settings.DB_NAME, host=settings.DB_HOST, port=settings.DB_PORT, io_loop=io_loop)
io_loop.start()