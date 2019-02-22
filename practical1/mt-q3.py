#!/usr/bin/env python3

'''Student Name: Van Linh Ha 
Student ID: vlha@myseneca.ca
Program: mt-q[3].py '''



def gpv():
	i = []
	grades = input("Please enter a list of grades: ")
	for x in grades.split():
		if x == "A":
			i.append(4)
		elif x == "B":
			i.append(3)
		elif x == "C":
			i.append(2)
		elif x == "D":
			i.append(3)
		elif x == "F":
			i.append(0)
	return i
def cal_gpa(mark):
	gpa = 0
	for a in mark:
		gpa += a
	return "Your GPA is " + str(gpa/len(mark))
if __name__ == '__main__':
	print(cal_gpa(gpv()))
	