#!/usr/bin/env python3

'''Student Name: Van Linh Ha 
Student ID: vlha@myseneca.ca
Program: mt-q[2].py '''

num = input("Plese enter five digits number: ")

try:
	test = int(num)

except:
	print(str(num) + " is not a number. Please try again.")
	exit()

if len(num) != 5:
	print(num + ' is not a five digits number. Please try again.') 
else:
	sum_num = 0
	for i in str(num):
		sum_num += int(i)
	print("Ok, the sum of the 5 digits of " + num + ' is ' + str(sum_num))