import pymongo, json, logging, time

from tornado.web import RequestHandler, authenticated
from models import User
from session import manager, Session
import settings

class BaseHandler(RequestHandler):

	def get_current_user(self):
		_t = manager.getSession(self.get_secure_cookie('userid'))
		return _t.userName if _t and _t.expireTime > int(time.time()) else None

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

		manager.delSession(self.get_secure_cookie('userid'))

		sess = Session(username)
		manager.addSession(sess)

		self.set_secure_cookie('userid', sess.sessionId)
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
		manager.delSession(self.get_secure_cookie('userid'))
		self.clear_cookie('userid')
		self.redirect('/login')

class Register(BaseHandler):

	def get(self):
		username = self.get_current_user()
		self.redirect('/') if username else self.render('iregister.html')

	def post(self):
		username, password = self.get_argument('username', ''), self.get_argument('password', '')
		if not self.isValid(username, password):  return self.write(json.dumps({'successful':False}))
		print 'hehe'
		user = User(username, password)
		settings.mongodb.user.insert(user.toMongoDB())
		self.write(json.dumps({'successful': True}))

	def isValid(self, username, password):
		return username and len(password) > 5

