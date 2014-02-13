import os

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.options import define, parse_command_line, options
from handlers import Index, Login, Logout, Register, Task

class GoApplication(Application):

	def __init__(self):

		handlers = [
			(r'/', Index),
			(r'/u/login', Login),
			(r'/u/logout', Logout),
			(r'/u/register', Register),

			(r'/d/data', Task),

			(r'/m/add', TasksAdd),
			(r'/m/delete', TasksDel),
			(r'/m/update', TasksUpdate),
		]

		settings = {
			'cookie_secret': 'tfdsaljfdsalgtel',
			'xsrc_cookies': True,
			'login_url': '/u/login', 
			'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
			'static_path': os.path.join(os.path.dirname(__file__), 'static'),
			'debug': True
		}
		
		super(GoApplication, self).__init__(handlers, **settings)

define('port', default=8989, type=int)
parse_command_line()
app = GoApplication()
app.listen(options.port)
IOLoop.instance().start()