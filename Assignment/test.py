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
		doy1 = time.strftime("%j",time1) # return day of year
		doy2 = time.strftime("%j",time2)
 
		if doy1 == doy2: # if same day
			print(time.mktime(time1),time.mktime(time2))
			total += abs(time.mktime(time1) - time.mktime(time2))
			record_list.append(item) # save the record to list
		else:
			next_day = time.mktime(time1) # float number
			while day1 != day2:
				eod_time = time.ctime(next_day).split()
				eod_time[3] = '23:59:59'

				eod_time_float = time.mktime(time.strptime(' '.join(eod_time))) # no need format because eod time has default strptime format

				y_second = eod_time_float - next_day
				print(y_second)

				next_day = next_day + 86400
				day1 = time.strftime('%j',time.localtime(next_day))

			print(total)
