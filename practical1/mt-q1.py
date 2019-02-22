#!/usr/bin/env python3

'''Student Name: Van Linh Ha 
Student ID: vlha@myseneca.ca
Program: mt-q[1].py '''

import sys

arg_num = len(sys.argv) -1 
res_list = []
for i in range(1,len(sys.argv)):
	res_list.append(sys.argv[i])

avg = 0
for x in res_list:
	avg += int(x)


print("Number of numbers received: ", arg_num)
print("List of numbers received: " , res_list)
print("Average for the given numbers: ", avg/len(res_list))