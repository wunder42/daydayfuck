import os

import tornado
from tornado.web import Application, RequestHandler, authenticated
from tornado import escape
from tornado.options import define, options, parse_command_line
from tornado.ioloop import IOLoop

define('port', default=8888, type=int)

class MainServer(object):
	_mainServer = None
	def __new__(self, *args, **kwargs):
		if not self._mainServer:
			self._mainServer = super(MainServer, self).__new__(self, *args, **kwargs)
		return self._mainServer

class Data(object):
	size = 100
	data = []
	def __init__(self):
		pass

	def __getitem__(self, index):
		if index < size:
			return self.data[index]

	def __getattr__(self, attr):
		if hasattr(self, attr):
			return self.__dict__[attr]

	def __iter__(self):
		for d in self.data:
			yield d

	def add_data(self, msg):
		if len(self.data) < self.size:
			self.data.append(msg)
			return True
		return False


class DataServer(object):

	handlers = set()
	def __init__(self):
		if hasattr(self, 'data'):
			return self.__getattr__('data')
		self.__setattr__('data', Data())

	def register_handler(self, handler):
		self.handlers.add(handler)

	def async_handler(self, msg):
		self.data.add_data(msg)
		for handler in self.handlers:
			handler(msg)
		self.handlers = set()

	def remove_handler(self, handler):
		self.handlers.remove(handler)
###
data_server = DataServer()

class BaseHandler(RequestHandler):

	def get_current_user(self):
		userJson = self.get_secure_cookie('chat_name') 
		if not userJson: return None
		return (userJson)

class HomeHandler(BaseHandler):
	@authenticated
	def get(self):
		# self.write('welcome %s' % self.get_current_user())
		self.messages = data_server.data
		self.render("ichat.html", title='ichat', iname=self.get_current_user())

class NewMsgHandler(BaseHandler):
	@authenticated
	def post(self):
		message = self.get_argument('content', None)
		if message:
			msg = {'src': self.current_user, 'content': message}
			data_server.async_handler(msg)
		#self.write('nice')
		# self.redirect('/')

class UpdateMsgHandler(BaseHandler):
	@authenticated
	@tornado.web.asynchronous
	def post(self):
		data_server.register_handler(self.on_new_message)

	def on_new_message(self, msg):
		if self.request.connection.stream.closed():
			return
		self.finish(msg)

	def on_connection_close(self):
		data_server.remove_handler(self.on_new_message)


class AuthLoginHandler(BaseHandler):
	def get(self):
		if self.get_argument('user', None):
			self.set_secure_cookie('chat_name',(self.get_argument('user')))
			self.redirect('/')
		self.render('login.html')


class AuthLogoutHandler(BaseHandler):
	@authenticated
	def get(self):
		self.clear_cookie('chat_name')
		self.redirect('/login')

if __name__ == '__main__':
	parse_command_line()
	app = Application(
		[(r'/', HomeHandler),
		 (r'/new_message', NewMsgHandler),
		 (r'/update_message', UpdateMsgHandler),
		 (r'/login', AuthLoginHandler),
		 (r'/logout', AuthLogoutHandler)
		],
		cookie_secret="tfdsaljfdsalgtel",
		xsrf_cookies=True,
		login_url="/login",
		template_path = os.path.join(os.path.dirname(__file__), 'templates'),
		debug=True
		)
	app.listen(options.port)
	IOLoop.instance().start()