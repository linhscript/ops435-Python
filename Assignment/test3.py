
if __name__ == '__main__':
	import time
	import os
	f = open('OPS435 Python A3 CCN Subscription - CDOT Wiki.html','r',encoding="utf8")
	data = f.readlines()
	f.close()
	print(data[0])