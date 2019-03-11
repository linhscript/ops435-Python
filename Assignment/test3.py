'''
OPS435 Assignment 3 - Winter 2018
Program: ccn_vlha.py
Author: Van Linh Ha
The python code in this file ccn_ccn_vlha.py is original work written by
Van Linh Ha. No code in this file is copied from any other source 
including any person, textbook, or on-line resource except those provided
by the course instructor. I have not shared this python file with anyone
or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and violators 
will be reported and appropriate action will be taken.
'''
import time
import os



if __name__ == '__main__':

	f = open('filename','r')
	data = f.readlines()
	f.close()
	data = ' '.join(map(str.strip,data))
	data = data.split('</tr>')
	data = data[0].split()
	print(data)

	dict1 = {}
	dict2 = {}
	for item in data:
		dict1[' '.join(data[0:2])] = data[3::]
		dict2[' '.join(data[0:2])] = data[2]
	print(" ")
	print(dict1,dict2)

