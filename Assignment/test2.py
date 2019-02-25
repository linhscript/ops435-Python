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
		time1 = time.strptime(' '.join(item.split()[3:8]),"%a %b %d %H:%M:%S %Y")
		time2 = time.strptime(' '.join(item.split()[9:14]),"%a %b %d %H:%M:%S %Y")
		# time1 and time2 is struct_time
		day1 = time.strftime("%j",time1) # return day of year
		day2 = time.strftime("%j",time2)
 
		if day1 != day2: # if same day
			next_day = time.mktime(time1) # float number
			while day1 != day2:
				eod_time = time.ctime(next_day).split()
				eod_time[3] = '23:59:59'

				new_info = item.split()
				new_info[9] = eod_time[0]
				new_info[10] = eod_time[1]
				new_info[11] = eod_time[2]
				new_info[12] = eod_time[3]
				new_info[13] = eod_time[4]							
				print(item.split())
				print(eod_time)
				print(new_info)

				y_second = eod_time_float - next_day
				print(y_second)

				next_day = next_day + 86400
				day1 = time.strftime('%j',time.localtime(next_day))
