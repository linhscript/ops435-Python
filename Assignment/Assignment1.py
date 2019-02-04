#!/usr/bin/env python3

def dbda(var1,var2):
	year = int(var1[0:4])
	month = int(var1[4:6])
	day = int(var1[6:])
	mon_max = leap_year(year)
	num = abs(int(var2))

	if int(var2) > 0:
		forward_day = day + num
		
		while forward_day > mon_max[month]:
			forward_day = forward_day - mon_max[month]
			month = month +1
			if month > 12:
				year = year + 1
				month = 1
				mon_max = leap_year(year)

		result = str(year)+str(month).zfill(2)+str(forward_day).zfill(2)
		print (result)
		return result

	else:
		backward_day = day - num

		while backward_day <= 0:
			month = month - 1
			if month == 0:
				month = 12
				year = year - 1
				mon_max = leap_year(year)
			backward_day = backward_day + mon_max[month]

		result = str(year)+str(month).zfill(2)+str(backward_day).zfill(2)
		print (result)
		return result


def leap_year(year_value):
	if (year_value % 4 == 0):
		if (year_value % 100 == 0):
			if (year_value % 400 ==0):
				feb = 29
			else:
				feb = 28
		else:
			feb = 29
	else:
		feb = 28
    ## Done Check Leaf year
	mon_max = { 1:31, 2:feb, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}	
	return mon_max

def validate(var1):
	if (len(var1) != 8):   # Check date format
		print("Wrong date format")
		exit()
	else:
		year = int(var1[0:4])
		month = int(var1[4:6])
		day = int(var1[6:])
		mon_max = leap_year(year)

	    # Check month and day are valid or not
		if month not in mon_max.keys():
			print("Wrong month input")
			exit()
		else:
			day_max = mon_max[month]
			if day not in range (1,day_max+1):    ### Plus 1 to take the last value
				print("Wrong day input")
				exit()


def tomorow(var1):
	validate(var1)
	year = int(var1[0:4])
	month = int(var1[4:6])
	day = int(var1[6:])
	mon_max = leap_year(year)
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
	
def yesterday(var1):
	validate(var1)
	year = int(var1[0:4])
	month = int(var1[4:6])
	day = int(var1[6:])
	mon_max = leap_year(year)
	yst_day = day - 1
	if yst_day == 0:
		month = month - 1
		if month == 0:
			year = year -1
			month = 12
			yst_day = 31
		else:
			yst_day = mon_max[month]

	day_before = str(year)+str(month).zfill(2)+str(yst_day).zfill(2)
	print(day_before)
	return day_before


	

#def yesterday(var1, num)


if __name__ == "__main__":
	var1 = '20180523'
	var2 = '-1700'
	var3 = '-365'
	dbda(var1,var2)
	#dbda(var1,var3)
	#validate(var1)
	#tomorow(var1)
	#yesterday(var1)
	#leap_year(var1)