import tornado.ioloop
import tornado.web

import os

class BaseHandler(tornado.web.RequestHandler):
	def get_current_user(self):
		return self.get_secure_cookie('user')

class MainHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		if not self.get_cookie('user'):
			# self.set_cookie('knife', 'pen knife')
			self.redirect('/login')
			return
		# self.write('pen knife')
		items = ['knife', 'apple', 'house']
		self.render('base.html', title='Base', items=items)

class LoginHandler(BaseHandler):
	def get(self):
		self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')
	def post(self):
		self.set_secure_cookie('user', self.get_argument('name'))
		self.redirect('/')

tornado.web.UIModule

settings= {
	'cookie_secret':'fdsafewrewew324',
	'login_url': '/login',
	'xsrf_cookies': True,
	'static_path': os.path.join(os.path.dirname(__file__), 'static'),
}

application = tornado.web.Application([
	(r'/', MainHandler),
	(r'/login', LoginHandler),
], **settings)

if __name__ == '__main__':
	application.listen(1000)
	tornado.ioloop.IOLoop.instance().start()