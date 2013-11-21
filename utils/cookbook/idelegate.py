#! /usr/bin/python

def t(f):
	def t1(x):
		print 'yy'
		return f(x)
		# return 3
	return t1

def t_(f):
	def t1():
		print 'yy_'
		print f()
		return 2
	return t1
@t_
@t
def k(*args, **kwargs):
	print 'xx'	

# print k()
print t(lambda x: x+1)(1)

# def tt(arg):
# 	print arg
# 	def ttt(f):
# 		def tttt(*args, **kwargs):
# 			val = f(*args, **kwargs)
# 			return val
# 		return tttt
# 	return ttt

# @tt('i')
# def kk(*args, **kwargs):
# 	print 'kk'
# 	return len(*args), args

# print kk([1, 2, 3])