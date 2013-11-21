#! -*- coding=utf-8 -*- 

def encrypt():
	import crypt
	print crypt.crypt('maomao', '0GFXe2cf')

	import hashlib

	hash = hashlib.md5()
	hash.update(u'maomao')
	print hash.digest().encode('utf-8')

	a = u'小刀'
	print a.encode('utf-8')

def main():
	encrypt()

# import crypt
# import random,string

# def getsalt(chars = string.letters+string.digits):
#     return random.choice(chars)+random.choice(chars)

# salt = getsalt()
# print salt
# print crypt.crypt('bananas',salt)


if __name__ == '__main__':
	main()