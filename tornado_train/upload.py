#! -*- coding: utf-8 -*-

import os, StringIO, json

import tornado
from tornado.web import Application, RequestHandler
from tornado.options import options, define, parse_command_line
from tornado.ioloop import IOLoop
from tornado import escape

import logging

define("port", default=4399, type=int)
logging.basicConfig(filename="upload.log", level = logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s", filemode="a")


class ImageMixin(object):

	def save(self, base_path, filename):
		pass

	def set_filename(self):
		pass

class Upload(RequestHandler):

	def get(self):
		self.render("upload.html")

	def post(self):
		logging.info('async upload file')

		try:
			content = StringIO.StringIO(self.request.files.get('upload', None)[0].get('body'))
			with open("haha.jpg", "wb") as f:
				for chunk in content.readlines():
					f.write(chunk)
		except Exception as e:
			logging.info(e)

		# self.write({'status':'success'})
		self.write(json.dumps({'status':'success'}))

class Uuu(RequestHandler):

	def get(self):
		logging.info('debug')
		self.render("upload.html")

	def post(self):
		logging.info('debug')
		try:
			content = StringIO.StringIO(self.request.files.get('uploads', None)[0].get('body'))
			with open("haha.jpg", "wb") as f:
				for chunk in content.readlines():
					f.write(chunk)
		except Exception as e:
			logging.info(e)

		# self.write('ok')
		# self.redirect('/u')
		self.render("upload.html")



class IApplication(Application):

	def __init__(self, *args, **kwarg):
		
		handlers = [
			(r'/', Upload),
			(r'/u', Uuu)
		]

		settings = {
			"xsrf_cookies": True,
			"cookie_secret":'cc0c1f98-9ed4-4abb-ab57-e80a13d2199e',
			"template_path": os.path.join(os.path.dirname(__file__), 'templates'),
			"static_path": os.path.join(os.path.dirname(__file__), 'static'),
			"debug":True
		}

		super(IApplication, self).__init__(handlers, **settings)


if __name__ == '__main__':
	parse_command_line()
	application = IApplication()
	application.listen(options.port)
	IOLoop.instance().start()