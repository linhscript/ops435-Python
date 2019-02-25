def read_login_rec(filelist):

	f = open(filelist,'r')
	login_rec = f.readlines()
	f.close()
	return login_rec
if __name__ == '__main__':
	import time
	
	filelist = 'usage_data_file'
	test = read_login_rec(filelist)
	l = []
	print(test)

