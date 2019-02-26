
if __name__ == '__main__':
	import time
	import os
	cmd = "last -Fiw"
	p = os.popen(cmd)  
	result = p.readlines()
	p.close() 
	login_recs = []
	for item in result:
		if len(item.split()) == 15: 
			login_recs.append(item)
	print(login_recs)