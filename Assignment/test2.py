def read_login_rec(filelist):

	f = open(filelist,'r')
	login_rec = f.readlines()
	f.close()
	return login_rec

if __name__ == '__main__':
	import time

	filelist = 'usage_data_file'
	test = read_login_rec(filelist)
	result = test[0].split()
	#print(result)

	t = (2009, 2, 17, 17, 3, 38, 8, 48, 0)
	t = time.strftime('%b %d %Y %H:%M:%S',t)
	print(t)