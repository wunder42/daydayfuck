#! -*- coding:utf-8 -*-
import pymongo, json, logging
from uuid import uuid5

import settings

class Session(object):

	def __init__(self, username, nickname):
		self.sessionId = uuid5('xdbhf', username + str(int(time.time())))
		self.userName = username
		self.nickname = nickname
		self.expireTime = int(time.time()) + settings.EXPIRE_TIME
		self.isOnline = True

	def __str__(self):
		return json.dumps(self.__dict__)

class SessionManager(object):

	def __init__(self):
		self.sessions = []

	def addSession(self, sess):
		self.sessions.append(sess)

	def delSession(self, sess):
		self.sessions.remove(sess)

	def onlineNum(self):
		return len(sessions)

	def findSession(self, sess):
		_t = db.sessions.find_one(sess)
		if not _t: return False
		# _t = json.loads(_t)
		if sess.expireTime < time.time():
			db.sessions.remove(_t)
			return False
		sess.isOnline = True
		db.sessions.update({'userName':sess.userName}, {$set, {'isOnline':True}})
		self.addSession(sess)
		return True

if __name__ == '__main__':
	sess = Session('knife@163.com', 'fly knife')
	print sess