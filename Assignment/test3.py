def read_login_rec(filelist):

	f = open(filelist,'r')
	login_rec = f.readlines()
	f.close()
	return login_rec
if __name__ == '__main__':
	import time
	
	filelist = 'test_data'
	test = read_login_rec(filelist)
	l = []
	for i in test:
		l.append(i.split().copy())
		print(i)
	print(l)