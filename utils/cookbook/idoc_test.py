#! /usr/bin/python

def test(x):
	'''
	>>> test(2)
	4
	>>> test(3)
	9
	'''
	return x * x

if __name__ == '__main__':
	import doctest, idoc_test
	doctest.testmod()