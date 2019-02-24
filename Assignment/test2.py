def read_login_rec(filelist):

	f = open(filelist,'r')
	login_rec = f.readlines()
	f.close()
	return login_rec

if __name__ == '__main__':
	import time
	
	filelist = 'usage_data_file'
	test = read_login_rec(filelist)
	result = test[0].split()
	#print(result)
	#Tue Feb 13 16:22:00 2018 - Tue Feb 13 16:45:00 2018
	a = time.strptime("Tue Feb 13 16:53:42 2018","%a %b %d %H:%M:%S %Y")
	b = time.strptime("Tue Feb 13 16:57:02 2018","%a %b %d %H:%M:%S %Y")
	c = time.strptime("Tue Feb 13 16:22:00 2018","%a %b %d %H:%M:%S %Y")
	d = time.strptime("Tue Feb 13 16:45:00 2018","%a %b %d %H:%M:%S %Y")

	#print(a)
	#print(b)
	s = time.strftime("%H:%M:%S",a)
	j = time.strftime("%H:%M:%S",b)

	#print(s)
	#print(j)
	res1 = time.mktime(a)
	res2 = time.mktime(b)
	res3 = time.mktime(c)
	res4 = time.mktime(d)	
	total1 = abs(res1-res2)
	total2 = abs(res3-res4)
	total = total1+total2
	print(total)
	#print(time.mktime(s))
