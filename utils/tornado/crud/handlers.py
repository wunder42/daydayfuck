import json

from tornado import gen
import tornado.web
from models import Todo

class BaseHandler(tornado.web.RequestHandler):

	def get_current_user(self):
		return True

class IndexHandler(BaseHandler):

	@tornado.web.asynchronous
	def get(self):
		''''''
		# self.write(json.dumps({'status':'OK'}))
		Todo.objects.find_all(callback=self._finish_get)

	def _finish_get(self, result):
		# self.finish(json.dumps({'result':result}))
		if isinstance(result, list):
			result = [c.content for c in result]
		self.finish(json.dumps({'result':result}))


class AddHandler(BaseHandler):

	@tornado.web.asynchronous
	def get(self):
		''''''
		self.content = self.get_argument('content', None)
		if not self.content: self.finish({'status':'ERROR'})
		Todo.objects.filter(content=self.content).find_all(self._finish_find)

	def _finish_find(self, result):
		print result
		if len(result): return self.finish({'verbose':'exist'})
		todo = Todo(content=self.content)
		todo.save(self._finish_save)

	def _finish_save(self, todo):
		try:
			assert todo is not None
		except Exception as e:
			return self.finish(json.dumps({'status':'SAVE ERROR'}))
		return self.finish(json.dumps({'status':'OK'}))

class DeleteHandler(BaseHandler):

	@tornado.web.asynchronous
	def get(self):
		''''''
		content = self.get_argument('content', None)
		Todo.objects.filter(content=content).find_all(self._finish_find)

	def _finish_find(self, result):
		if len(result):
			result[0].delete(self._finish_del)
		else: return self.finish('delete error')

	def _finish_del(self, result):
		if result: return self.finish('delete true')
		return self.finish('delete error')


class UpdateHandler(BaseHandler):

	@tornado.web.asynchronous
	def get(self):
		''''''
		key = self.get_argument('key', None)
		self.content = self.get_argument('content', None)
		Todo.objects.filter(content=key).find_all(self._finish_update)

	def _finish_update(self, result):
		if len(result):
			result[0].content = self.content
			result[0].save(self._finish_save)
		else: return self.finish('error')

	def _finish_save(self, todo):
		try:
			assert todo is not None
		except Exception as e:
			return self.finish(json.dumps({'status':'SAVE ERROR'}))
		return self.finish(json.dumps({'status':'OK'}))

class TestHandler(BaseHandler):

	@tornado.web.asynchronous
	def get(self):
		''''''
		content = self.get_argument('content', None)
		todo = Todo(content=content)
		todo.save(self._finish_save)

	def _finish_save(self, todo):
		try:
			assert todo is not None
		except Exception as e:
			return self.finish(json.dumps({'status':'SAVE ERROR'}))
		return self.finish(json.dumps({'status':'OK'}))