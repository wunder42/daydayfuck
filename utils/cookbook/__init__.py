import heapq

def _heap():
	s = [1, 2, 3, 4, 5, 6]
	print heapq.nlargest(3, s)

def main():
	_heap()

if __name__ == '__main__':
	main()