#!/usr/bin/env python3
'''
OPS435 Assignment 1 - Fall 2018
Program: [vlha].py (replace vlha with your Seneca User name)
Author: "Linh Van Ha"
The python code in this file ([vlha.py) is original work written by
"Linh Van Ha". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import sys


def usage ():
	if sys.argv[1] == '--step':
		if len(sys.argv) != 4: 
			print (sys.argv[0] + '--step' +'YYYYMMDD' + '-/+')
			exit()
	else:
		if len(sys.argv) != 3: 
			print (sys.argv[0]  +'YYYYMMDD' + '-/+')
			exit()


def dbda(var1,var2):
	'''
	The dbda() function will take a date in "YYYYMMDD" format,
	a positive or negative integer, and return a date either before 
	or after the given date according to the value of the given integer in the same format.
	'''
	i = 0
	result = var1
	if int(var2) > 0: # When var2 is positive (calculate day forward)
		while i < int(var2):  # Plus one day until i not less than thw 
			i += 1
			result = tomorrow(result)
			
	elif int(var2) < 0:  # When var2 is negative (calculate day backward)
		while i > int(var2):
			result = yesterday(result)
			i = i - 1
			
	else:
		result = result

	return result

def leap_year(year_value):
	'''
	The leapyear() function will take a year in "YYYY" format, 
	and return True if the given year is a leap year, otherwise return False.
	'''
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
	'''
	The validdate() function will take a date in "YYYYMMDD" format, 
	and return True if the given date is a valid date, otherwise return False.
	'''
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


def tomorrow(var1):
	'''
	The tomorrow() function will take a date in "YYYYMMDD" format and return the date of the next day in the same format.
	Next paragraph is a sample python code for the tomorrow() function.
	'''
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
	return next_date
	
def yesterday(var1):
	'''
	The yesterday() function will take a date in "YYYYMMDD" format 
	and return the date of the previous day in the same format.
	'''
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
	return day_before


	
if __name__ == "__main__":
	usage()	
	sys.argv[1] == '--step'
	if sys.argv[1] == '--step':
		var1 = sys.argv[2]
		var2 = sys.argv[3]
	else:
		var1 = sys.argv[1]
		var2 = sys.argv[2]

	print(dbda(var1,var2))



	#dbda(var1,var3)
	#validate(var1)
	#tomorow(var1)
	#yesterday(var1)
	#leap_year(var1)
