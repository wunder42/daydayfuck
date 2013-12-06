import json

class User(object):
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def __str__(self):
		# return '"%s"' % json.dumps(self.__dict__)
		return json.dumps(self.__dict__)

	def toMongoDB(self):
		return self.__dict__

if __name__ == '__main__':
	user = User('aaa', 'bbb')
	print user.toMongoDB()