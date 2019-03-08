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
def gen_text(option):
	if option == True:
		print("Files to be processed: ",args.filename)
		print("Type of args for files ",type(args.filename))

		if args.list:
			print("usage report for user: ",subject)
			print("usage report type: ",args.type)
			print("processing usage report for the following:")
			print("reading login/logout record files ",args.filename)
		else:
			print("processing usage report for the following:")
			print("reading login/logout record files ",args.filename)
			print("Generating list for ",args.list)


if __name__ == '__main__':
	import time
	import os
	#f = open('test_data','r')
	#data = f.read()
	#f.close()
	#print(data.split())
	gen_text()