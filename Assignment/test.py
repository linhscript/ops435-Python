#!/usr/bin/env python3

#file = usage_data_file
f = open('usage_data_file','r')
a = f.readlines()
f.close()
#all_name = {}
for name in a:
	all_name.append(name.split()[0])
for item in all_name:

