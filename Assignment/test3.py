
if __name__ == '__main__':
	import time
	import os
	f = open('test_data','r')
	data = f.read()
	f.close()
	print(data.split())