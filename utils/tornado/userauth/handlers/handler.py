import pymongo, json, logging

from tornado.web import RequestHandler, authenticated
from models import User
import settings

# logging.basicConfig(filename="userauth.log", format="%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s", level=logging.DEBUG)

class BaseHandler(RequestHandler):

	def get_current_user(self):
		return self.get_secure_cookie('userid')

	def update_session(self):
		pass

class Home(BaseHandler):

	@authenticated
	def get(self):
		self.write(json.dumps({'login':True, 'username':self.get_current_user()}))

class Login(BaseHandler):

	def get(self):
		if self.get_current_user(): return self.redirect('/')
		self.render('ilogin.html')

	def post(self):
		username, password = self.get_argument('username', ''), self.get_argument('password', '')
		if not self.isValid(username, password): return self.write(json.dumps({'successful':False}))
		logging.info('login valid')
		self.set_secure_cookie('userid', username)
		self.write(json.dumps({'successful':True}))

	def isValid(self, username, password):
		if not username or len(password) < 6: return False
		user = User(username, password)
		_t = settings.mongodb.user.find_one(user.toMongoDB())
		logging.info(_t)
		if _t: return True
		return False

class Logout(BaseHandler):

	@authenticated
	def get(self):
		self.clear_cookie('userid')
		self.redirect('/login')

class Register(BaseHandler):

	def get(self):
		userid = self.get_current_user()
		self.redirect('/') if userid else self.render('iregister.html')

	def post(self):
		username, password = self.get_argument('username', ''), self.get_argument('password', '')
		if not self.isValid(username, password):  return self.write(json.dumps({'successful':False}))
		print 'hehe'
		user = User(username, password)
		settings.mongodb.user.insert(user.toMongoDB())
		self.write(json.dumps({'successful': True}))

	def isValid(self, username, password):
		return username and len(password) > 5

