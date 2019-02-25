def read_login_rec(filelist):

	f = open(filelist,'r')
	login_rec = f.readlines()
	f.close()
	return login_rec

if __name__ == '__main__':
	import time
	
	filelist = 'test_data'
	test = read_login_rec(filelist)
	result = test[1].split()
	
	time1 = time.strptime(' '.join(result[3:8]),"%a %b %d %H:%M:%S %Y") # struct_time
	time2 = time.strptime(' '.join(result[9:14]),"%a %b %d %H:%M:%S %Y") # struct_time
	day1 = time.strftime('%j',time1) #---> day of year
	day2 = time.strftime('%j',time2)
	t = time.ctime(time.mktime(time1)).split()
	t[3] = '23:59:59'
	print(result[3:8],result[9:14])
	print(t)
	print(time.ctime(time.mktime(time1)))

	print(test[1])
	

	#Tue Feb 13 16:53:42 2018
	record_list = result.copy()
	print(record_list)
	next_day = time.mktime(time1) # float number
	while day1 != day2:
		eod_time = time.ctime(next_day).split()
		eod_time[3] = '23:59:59'

		eod_time_float = time.mktime(time.strptime(' '.join(eod_time))) # no need format because eod time has default strptime format

		y_second = eod_time_float - next_day
		print(y_second)

		next_day = next_day + 86400
		day1 = time.strftime('%j',time.localtime(next_day))



	
	
