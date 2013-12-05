import pymongo, json, logging

from tornado.web import RequestHandler, authenticated
import settings


class BaseHandler(RequestHandler):

	def get_current_user(self):
		return self.get_secure_cookie('user_id')

	def update_session(self):
		pass

class Login(BaseHandler):

	def get(self):
		if self.get_current_user(): self.redirect('/')
		self.render('login.html')

	def post(self):
		username, password = self.get_argument('username', ''), self.get_argument('password', '')
		if not self.isValid(username, password): return self.write(json.dumps('successful':False))

		logging.info('login valid')
		self.write(json.dumps('successfule':True))

	def isValid(self, arguments):
		return True
		

class Logout(BaseHandler):

	@authenticated
	def get(self):
		self.clear_cookie('user_id')
		self.redirect('/login')

class RegisterUser(BaseHandler):

	def get(self):
		userId = self.get_secure_cookie('user_id')
		self.redirect('/') if userId else self.render('register.html')

	def post(self):
		username, password = self.get_argument('username', ''), self.get_argument('password', '')
		if not self.isValid(username, password):  return self.write(json.dumps('successful':False))
		user = User(username, password)
		mongo.insert('user', user)
		self.write(json.dumps({'successful': True}))

	def isValid(self, username, password):
		return len(arguments.get('username', '')) and len(arguments.get('password', '')>5)
