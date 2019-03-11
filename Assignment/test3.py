'''

'''


if __name__ == '__main__':
	import time
	import os
	f = open('filename.txt','r')
	data = f.readlines()
	f.close()
	data = ' '.join(map(str.strip,data))
	print(data)
	print("")
	data = data.split('</tr>')
	data = data[0].split()
	print(data)
