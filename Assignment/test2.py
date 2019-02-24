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
	time1 = time.strptime(' '.join(result[3:8]),"%a %b %d %H:%M:%S %Y")
	
	print(time1)
	
