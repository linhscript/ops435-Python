#!/usr/bin/env python3
#import sys
#print(sys.version)
def validate(var1):
	if (len(var1) != 8):
		print("Wrong date format")
		exit()
	else:
		year = int(var1[0:4])
		month = int(var1[4:6])
		day = int(var1[6:])
	    
		if (year % 4 == 0):
			if (year % 100 == 0):
				if (year % 400 ==0):
					feb = 29
				else:
					feb = 28
			else:
				feb = 29
		else:
			feb = 28
	    ## Done Check Leaf year

		mon_max = { 1:31, 2:feb, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}


	    # Check month and day are valid or not
		if month not in mon_max.keys():
			print("Wrong month input")
		else:
			day_max = mon_max[month]
			if day not in range (1,day_max+1):    ### Plus 1 to take the last value
				print("Wrong day input")

		return mon_max

def tomorow(var1):
	mon_max = validate(var1)
	year = int(var1[0:4])
	month = int(var1[4:6])
	day = int(var1[6:])

	tmr_day = day + 1
	
	if tmr_day > mon_max[month]: 
		tmr_day = 1
		month = month + 1
		if month > 12:
			month = 1
			year = year + 1

	next_date = str(year)+str(month).zfill(2)+str(tmr_day).zfill(2)
	print (next_date)
	return next_date


if __name__ == "__main__":
	var1 = '2019013'
	tomorow(var1)