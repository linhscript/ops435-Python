def read_login_rec(filelist):

	f = open(filelist,'r')
	login_rec = f.readlines()
	f.close()
	return login_rec
if __name__ == '__main__':
	import time
	
	filelist = 'test_data'
	test = read_login_rec(filelist)
	total = 0
	record_list = []
	for item in test:
		time1 = time.strptime(' '.join(item.split()[3:8]),"%a %b %d %H:%M:%S %Y")
		time2 = time.strptime(' '.join(item.split()[9:14]),"%a %b %d %H:%M:%S %Y")
		# time1 and time2 is struct_time
		doy1 = time.strftime("%j",time1) # return day of year
		doy2 = time.strftime("%j",time2)
 
		if doy1 == doy2: # if same day
			print(time.mktime(time1),time.mktime(time2))
			total += abs(time.mktime(time1) - time.mktime(time2))
		else:
			#while doy1 != doy2:
			print('87,780 seconds in total and 60,300 seconds in 14 and (27,479+200=27679) in 13')

	print(total)
