'''
Files to be processed: ['a2_test_data_2']
Type of args for files <class 'list'>

usage report for user: user5
usage report type: weekly
processing usage report for the following:
reading login/logout record files ['a2_test_data_2']

Files to be processed: ['a2_test_data_2']
Type of args for files <class 'list'>

processing usage report for the following:
reading login/logout record files ['a2_test_data_2']
Generating list for host

'''
def gen_text():
	print("Files to be processed: ",args.filename)
	print("line1\nType of args for files <class 'list'>")

if __name__ == '__main__':
	import time
	import os
	#f = open('test_data','r')
	#data = f.read()
	#f.close()
	#print(data.split())
	gen_text()