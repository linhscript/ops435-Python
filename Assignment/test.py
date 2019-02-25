def read_login_rec(filelist):

	f = open(filelist,'r')
	login_rec = f.readlines()
	f.close()
	return login_rec

def cal_daily_usage(subject,login_recs):
    ''' docstring for this function
    generate daily usage report for the given 
    subject (user or remote host)'''
    text = "Daily Usage Report for "
    print(text+str(subject))
    print(len(text+str(subject))*'=')
    print("Date"+" "*10+"Usage in Seconds")
    
    #return daily_usage
if __name__ == '__main__':
	import time
	
	filelist = 'usage_data_file'
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
			record_list.append(item.split()) # save the record to list
		else: # this works even jump to many days
			next_day = time.mktime(time1) # float number
			
			eod_time = time.ctime(next_day).split() #convert to readable time
			old_day = item.split()

			old_day[9] = eod_time[0]
			old_day[10] = eod_time[1]
			old_day[11] = eod_time[2]
			old_day[12] = '23:59:59'
			old_day[13] = eod_time[4]							
			record_list.append(old_day)
			while doy1 != doy2:
								
				next_day = next_day + 86400 #floating number
				new_day = item.split()
				new_time = time.ctime(next_day).split() # covert to readable time
				new_day[3] = new_time[0]
				new_day[4] = new_time[1]
				new_day[5] = new_time[2]
				new_day[6] = '00:00:00'
				new_day[7] = new_time[4]
				doy1 = time.strftime('%j',time.localtime(next_day))

				if doy1 != doy2: # check if next day is on the same day with end day or not
					new_day[9] = new_time[0]
					new_day[10] = new_time[1]
					new_day[11] = new_time[2]
					new_day[12] = '23:59:59'
					new_day[13] = new_time[4]
				record_list.append(new_day)
	
	cal_daily_usage('rchan',login_rec)

