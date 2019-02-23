#!/usr/bin/env python3

#file = usage_data_file
def read_login_rec(filelist):

	f = open(filelist,'r')
	login_rec = f.readlines()
	f.close()
	return login_rec

def get_list (list_record,position):
	res_list = set()
	for item in list_record:
		res_list.add(item.split()[position])

	for i in res_list:
		print (i)

if __name__ == '__main__':
	import argparse
	filename = 'usage_data_file'
	parser = argparse.ArgumentParser(description = "Usage Report based on the last command",
	 epilog = "Copyright 2018 - Linh Van Ha")
	parser.add_argument('F', help='generate user name or remote host IP from the given files')
	parser.add_argument('-l {user,host}', '--list', choices = ['user','host']
		,help='generate user name or remote host IP from the given files')
	parser.add_argument('-r', '--rhost', help='usage report for the given remote host IP')
	args = parser.parse_args()

###################################################################


	login_rec = read_login_rec (filename)
	if args.list == 'user':
		number = 0
	else:
		number = 2
	get_list (login_rec,number)