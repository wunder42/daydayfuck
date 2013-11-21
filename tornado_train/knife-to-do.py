#! -*- coding=utf-8 -*-
import os, time

from tornado import web
from tornado.web import RequestHandler, Application, authenticated
from tornado import ioloop, escape
from tornado.options import define, options, parse_command_line

import pymongo

### mongodb ###
connection = pymongo.Connection('127.0.0.1', 27017)
ndb = connection.inote 


define("port", default=1314, type=int)

class IApplication(Application):

	def __init__(self, *args, **kwargs):
		# super(Application, self).__init__(*args, **kwargs)

		handlers = [
			(r'/', IHome),
			(r'/login', ILogin),
			(r'/logout', ILogout),
			(r'/register', IRegister),

			(r'/n/add', IAddNote),
			(r'/n/delete/(\d+)', IDelNote),
			(r'/n/update/(\d+)', IUpdateNote),
			(r'/n/search/(\w+)', ISearchNote)
		]

		settings = {
			"login_url": "/login",
			"cookie_secret": "cc5f6f19-186f-4f72-8016-357f1211b436",
			"xsrf_cookies": True,
			"debug": True,
			"template_path": os.path.join(os.path.dirname(__file__), "templates"),
			"static_path": os.path.join(os.path.dirname(__file__), "static")
		}

		super(IApplication, self).__init__(handlers, **settings)

class BaseHandler(RequestHandler):

	def __init__(self, *args, **kwargs):
		super(BaseHandler, self).__init__(*args, **kwargs)

	def get_current_user(self):
		user = self.get_secure_cookie("user", None)
		return user if user else None

class IHome(BaseHandler):

	@authenticated
	def get(self):
		# notes = ['写一个Tornado的Demo', '记20个英文单词', '读一篇英语文章', '看～～爸爸去哪儿', '去吃夜宵', '写一个Tornado的Demo', '记20个英文单词', '读一篇英语文章', '看～～爸爸去哪儿', '去吃夜宵', '写一个Tornado的Demo', '记20个英文单词', '读一篇英语文章', '看～～爸爸去哪儿', '去吃夜宵']
		notes = ndb.inote_table.find().sort("nid", pymongo.DESCENDING)
		self.render("ihome.html", notes=notes)

class IAddNote(BaseHandler):

	def get(self):
		self.write('ok')

	@authenticated
	def post(self):
		content = self.get_argument("content", None)
		response = {'status':False}
		if content:
			inote_table = ndb.inote_table
			# nid = reduce(lambda x, y: max(x, y), inote_table.find())
			try:
				nid = inote_table.find().sort("nid", pymongo.DESCENDING)
				nid = nid[0].get('nid', 0) + 1 if nid else 0
			except IndexError, e:
				nid = 0
			inote_table.insert({'nid': nid, 'user': self.current_user, \
				'create-timestamp': int(time.time()*1000), 'content': content, \
				'update-timestamp': None, 'clock-deadline': None})
			# inote_table.save()
			response['nid'] = nid
			response['status'] = True
			response['content'] = content
		response = escape.json_encode(response)
		self.write(response) 

class IDelNote(BaseHandler):

	@authenticated
	def get(self, nid):
		pass

class IUpdateNote(BaseHandler):

	@authenticated
	def post(self, nid):
		pass

class ISearchNote(BaseHandler):

	@authenticated
	def get(self, nkey_word):
		pass

#### user ####

class ILogin(RequestHandler):

	def get(self):
		user = self.get_secure_cookie("user", None)
		self.redirect("/") if user else self.render("ilogin.html")

	def post(self):
		user = self.get_argument("user", None)
		inote_user_table = ndb.inote_user_table
		if user and inote_user_table.find_one({"user": user}):
			self.set_secure_cookie("user", user)
			# self.set_cookie_expire
			self.redirect('/')
		self.redirect('/register')

class IRegister(RequestHandler):

	def get(self):
		user = self.get_secure_cookie("user", None)
		self.redirect("/") if user else self.render("iregister.html")


	def post(self):
		user = self.get_argument("user", None)
		inote_user_table = ndb.inote_user_table
		if user and not inote_user_table.find_one({'user': user}):
			inote_user_table.insert({"user": user})
			# self.set_secure_cookie("user", user)
			return self.redirect('/login')
		self.write('error register')

class ILogout(RequestHandler):

	@authenticated
	def get(self):
		self.clear_cookie("user")
		self.redirect("/login")

if __name__ == '__main__':
	parse_command_line()
	app = IApplication()
	app.listen(options.port)
	ioloop.IOLoop.instance().start()