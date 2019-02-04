def leap_year(var1):
	year = int(var1[0:4])
    
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
	return mon_max

def dbda(var1,var2):
	mon_max = leap_year(var1)
	year = int(var1[0:4])
	month = int(var1[4:6])
	day = int(var1[6:])
	num = abs(int(var2))

	if int(var2) > 0:
		forward_day = day + num
		
		while forward_day > mon_max[month]:
			forward_day = forward_day - mon_max[month]
			month = month +1
			if month > 12:
				year = year + 1
				month = 1
				print (year)
				print(type(year))
				mon_max = leap_year('2019')
				print (mon_max)


		result = str(year)+str(month).zfill(2)+str(forward_day).zfill(2)
		print (result)
		return result


if __name__ == "__main__":
	var1 = '20180523'
	var2 = '+365'
	var3 = '-365'
	dbda(var1,var2)
	#dbda(var1,var3)
	#validate(var1)
	#tomorow(var1)
	#yesterday(var1)
	#leap_year(str(var1))