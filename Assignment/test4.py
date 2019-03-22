import time
import os


if __name__ == '__main__':

	f = open('line','r')
	data = f.readlines()
	f.close()
	data = ' '.join(map(str.strip,data))
	data = data.split('line')[1::]
	print("")
	print(data)


