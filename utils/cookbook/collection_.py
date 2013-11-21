from collections import deque, defaultdict, OrderedDict
# import queue

# d = deque(maxlen=3)
# d.append(1)

# print d.pop(), len(d)

d = defaultdict(list)
d['a'].append(1)
# print d

k = {}
k.setdefault('a', []).append(1)
# print k

def dictOrder():
	from operator import itemgetter, attrgetter
	a = [2, 3, 4, 9, 1]
	print sorted(a, reverse=True)

	b = [{'id':1, 'name':'maohj'}, {'id':3, 'name':'cheny'}, {'id':2, 'name':'liuzz'}]
	# print sorted(b, key=lambda x: x['name'])
	b = sorted(b, key=itemgetter('name'))
	for x in b: print x['id'],
	print 

	class T:
		def __init__(self, value): self.x = value
		# def __getitem__(self, key): 
		# 	# if self.get
		# 	return key

	c = [T(1), T(3), T(2)]
	# print sorted(c, key=itemgetter('x'))
	# c = sorted(c, cmp = lambda x, y : x.x - y.x)
	# c = sorted(c, key = lambda x : x.x)
	c = sorted(c, key = attrgetter('x'), reverse=True)
	for x in c: print x.x,
	t = T(1)
	# print t.x, t['x']

def main():
	dictOrder()

if __name__ == '__main__':
	main()