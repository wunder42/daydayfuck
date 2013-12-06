#! -*- coding:utf-8 -*-
import pymongo, json, logging, time, uuid
from uuid import uuid5

import settings

class Session(object):

	def __init__(self, username):
		self.sessionId = str(uuid5(uuid.NAMESPACE_DNS, str(int(time.time()))))
		self.userName = username
		self.expireTime = int(time.time()) + settings.EXPIRE_TIME
		self.isOnline = True

	def recoverSession(self, **k):
		self.__dict__ .update(**k)

	def __str__(self):
		return self.userName

	def toMongoDB(self):
		return self.__dict__

	def fromMongoDB(self, k):
		self.__dict__.update(k)

class SessionManager(object):

	@staticmethod
	def instance():
		if not hasattr(SessionManager, '_instance'):
			SessionManager._instance = SessionManager()
		return SessionManager._instance

	def __init__(self):
		self.sessions = {}

	def addSession(self, sess):
		self.sessions[sess.sessionId] = sess
		settings.mongodb.sessions.insert(sess.toMongoDB())

	def delSession(self, sessionId):
		if self.sessions.has_key(sessionId): del self.sessions[sessionId]
		settings.mongodb.sessions.remove({'sessionId':sessionId})

	def onlineNum(self):
		return len(sessions)

	def findSession(self, sess):
		_t = settings.mongodb.sessions.find_one(sess.toMongoDB())
		if not _t: return False
		if sess.expireTime < time.time():
			settings.mongodb.sessions.remove(sess.toMongoDB())
			return False
		# sess.isOnline = True
		# settings.mongodb.sessions.update({'userName':sess.userName}, {'$set', {'isOnline':True}})
		# self.addSession(sess)
		return True

	def getSession(self, sessionId):
		_sess = self.sessions.get(sessionId, None)
		if not _sess:
			_k = settings.mongodb.sessions.find_one({'sessionId':sessionId})
			if not _k: return None
			_sess = Session('anonymous')
			_sess.fromMongoDB(_k)
			self.sessions[_sess.sessionId] = _sess
		return _sess

	# def getSession(self, sessionId):
		# return self.sessions.get(sessionId, None)



manager = SessionManager.instance()

if __name__ == '__main__':
	sess = Session('knife@163.com')
	s = Sess
	print sess