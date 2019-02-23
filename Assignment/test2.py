#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Winter 2019
Program: [bpashalidis].py (replace student_id with your Seneca User name)
Author: "Bobby Pashalidis"
The python code in this file ([bpashalidis].py) is original work written by
"Bobby Pashalidis". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''

import sys


def usage ():
	'''
	This function checks if the user has input  an argument.
	If the user types the number of arguments diffrent than either 3 or 4, it explains how to use it correctly
	'''

	if ((len(sys.argv) != 4) and len(sys.argv) != 3): 
		print (sys.argv[0] + ' [--step]' +' YYYYMMDD' + ' -/+')
		exit()


        
def leap_year(date):
	'''
	This Function is the leap year function and checks if the year is a leap year with a T/F
	'''
	if (int(date) % 4 == 0):
		if (int(date) % 100 == 0):
			if (int(date) % 400 == 0):
				return "True"
			else:
				return "False"
		else:
			return "True"
	else:
		return "False"
													
		
def day_in_month(year):
	if leap_year(year):
		feb = 29
	else:
		feb = 28

	mon_max = { 1:31, 2:feb, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	return mon_max
	
def valid_date(date):
	'''
	This function checks if the date is correctly formatted and returns a T/F
	'''
	if len(date) != 8:
		print("False")
		exit()
	else:
		year = int(date[0:3])
		month = int(date[4:6])
		day = int(date[6:])
		days_dic = days_in_month(year) 
		if month not in days_dic.keys():
			print("False")
			exit()
		else:
			dayss = days_dic[month]
			if day not in range (1,daysss+1):
				print("False")
				exit()	
	return "True"
	
def yesterday(today):
	'''
	This function checks the date format and returns the previous day in format
	'''
	if len(today) != 8:
		return '00000000'
	else:
		year = int(today[0:4])
		month = int(today[4:6])
		day = int(today[6:])
															             
		tmp_day = day - 1 
																															                    
		mon_max = days_in_month(year)
		if tmp_day < mon_max[month]:
			to_day = tmp_day % mon_max[month] 
			tmp_month = month - 1
		else:
			to_day = tmp_day
			tmp_month = month - 0
																																															                     
		if tmp_month < 1:
			to_month = 12
			year = year - 1
			to_day = 31
		else:
			to_month = tmp_month + 0

		next_date = str(year)+str(to_month).zfill(2)+str(to_day).zfill(2)
     
		return next_date
		
def dbda(yyyymmdd,days):
	'''
	This function takes the date, and integers, then returns a date + or - the input date 
	'''
	if len(yyyymmdd) != 8:
		return "Error: wrong date entered"
		exit()
	else:
		year = int(yyyymmdd[0:3])
		month = int(yyyymmdd[4:6])
		day = int(yyyymmdd[6:])
		days_dic = days_in_month(year) 
		if month not in days_dic.keys():
			print("Error: wrong month entered")
			exit()
		else:
			daysss = days_dic[month]
			if day not in range (1,daysss+1):
				print("Error: wrong day entered")
				exit()	
	 
	target_day = str(yyyymmdd)
	counter = 0 
	if int(days) < 0:
		days = int(days) * -1
		while (counter != int(days)):
			target_day = yesterday(target_day)
			counter = counter +1
	else:
		while (counter != int(days)):
			target_day = tomorrow(target_day)
			counter = counter +1
	return target_day       

def days_in_month(year):
	'''
	This function checks day in a month based on leap year being T/F 
	'''
	leap = leap_year(int(year))
	if (leap == 'true'):
		days_month = 29
	else:
		days_month = 28
	days_mon = { 1:31, 2:days_month, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	return days_mon

if __name__ == '__main__':
	print(dbda(sys.argv[1], sys.argv[2]))

