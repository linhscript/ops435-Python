def read_login_rec(filelist):

	f = open(filelist,'r')
	login_rec = f.readlines()
	f.close()
	return login_rec
if __name__ == '__main__':
	import time
	
	filelist = 'test_data'
	login_rec = read_login_rec(filelist)
	total = 0
	record_list = []
	for item in login_rec:
		print(item.split())