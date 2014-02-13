import json
import logging
import asyncmongo
import settings
from session import AsyncMongoSession, asyncmongosession

import tornado.web
from tornado.web import RequestHandler, authenticated


logging.basicConfig(filename="gogogo.log", format="%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s", level=logging.DEBUG)

class BaseHandler(RequestHandler):

	@property
	def db(self):
		if not hasattr(self, 'db'):
			self._db = asyncmongo.Client(pool_id='gtd_pool', **settings.get('mongo_database'))
		return self._db

	# @property
	# def session(self):
	# 	self._session = None
	# 	return self._session

	# @session.setter
	# def session(self, value):
	# 	self._session = value

	def api_response(self, data):
		self.set_header("Content-Type", "application/javascript; charset=UTF-8")
		data = json.dumps(data)
		self.finish(data)

	def get_current_user(self):
		return True
		# self.get_secure_cookie('asyncmongo_session')

		# self.username = None

		# @asyncmongosession
		# def t(se):
		# # logging.info(self.get_secure_cookie('asyncmongo_session'))
		# # logging.info(self.session.get('username', None))

		# 	try:
		# 		self.username = se.session.get('username', None)
		# 	except Exception as e:
		# 		pass
		# 	return 'haha'
		# t(self)
		# return self.username
		# return username

class Index(BaseHandler):

	# @tornado.web.asynchronous
	# @asyncmongosession
	# def get(self):
	# 	username = self.session.get('username', None)
	# 	if not username:
	# 		# self.api_response({'status':'NG'})
	# 	self.render('gogogo.html')
	# 	self.finish()

	def get(self):
		self.render('gogogo.html')

class Login(BaseHandler):
	''''''
	@tornado.web.asynchronous
	@asyncmongosession
	def get(self):
		username = self.session.get('username', None)
		if not username:
			self.api_response({'status':'NG'})
		self.api_response({'status':'OK'})

	@tornado.web.asynchronous
	@asyncmongosession
	def post(self):
		# j = json.loads(self.request.body)
		# username, password = j.get('username', None), j.get('password', None)
		# self.set_secure_cookie('user', username)
		# self.write(json.dumps({'login_status':True}))

		# username, password = self.get_argument('username', ''), self.get_argument('password', '')
		if settings.REST_DEBUG:
			username, password = self.get_argument('username', ''), self.get_argument('password', '')
		else:
			j = json.loads(self.request.body)
			username, password = j.get('username', ''), j.get('password', '')
		try:
			self.db.user.find_one({'username':username, 'password':password}, callback=self.async_callback(self._finish_login))
		except Exception as e:
			logging.info(e)
			self.api_response({'login_status':False})

	def _finish_login(self, response, error):
		if error or len(response) == 0:
			logging.info(error)
			self.api_response({'status':'NG'})

		self.session['username'] = response.get('username', None)
		self.api_response({'status':'OK', 'login_status': 'record(%s) login' % response})


class Register(BaseHandler):
	''''''

	@tornado.web.asynchronous
	def post(self):
		# username, password = self.get_argument('username', ''), self.get_argument('password', '')
		if settings.REST_DEBUG:
			username, password = self.get_argument('username', ''), self.get_argument('password', '')
		else:
			j = json.loads(self.request.body)
			username, password = j.get('username', ''), j.get('password', '')

		if not self.isValid(username, password):
			self.api_response({'register_status':False, 'verbose':'error username or password'})

		try:
			self.db.user.insert({'username':username, 'password':password}, callback=self.async_callback(self.finish_register))
		except Exception as e:
			logging.info(e)
			self.api_response({'register_status':False, 'verbose':'error register'})

	def finish_register(self, response, error):
		if error or response[0].get('ok') != 1:
			logging.info(error)
			raise tornado.web.HTTPError(500, 'QUERY_ERROR')

		self.api_response({'status':'OK', 'register_status': 'record(%s) saved' % response})

	def isValid(self, username, password):
		if username != '' and password != '':
			return True
		return False

class Logout(BaseHandler):
	''''''
	def get(self):
		self.clear_cookie('username')
		self.write(json.dumps({'status':'OK', 'logout': True}))

class Task(BaseHandler):

	@tornado.web.asynchronous
	@asyncmongosession
	def get(self):
		username = self.session.get('username', None)
		if not username:
			self.api_response({'status':'NG'})
		self.api_response({'status':'OK'})

class TasksAdd(BaseHandler):

	@tornado.web.asynchronous
	@asyncmongosession
	def post(self):
		username = self.session.get('username', None)
		if not username:
			self.api_response({'status':'NG'})

		try:
			data = {'username':username, 'category':['']}
			self.db.data.insert({'username':username, 'password':password}, callback=self.async_callback(self.finish_register))
		except Exception as e:
			logging.info(e)
			self.api_response({'status':'NG', 'verbose':'ERROR REQUEST'})

	def _finish_add(self):
		self.api_response({'status':'OK'}) 