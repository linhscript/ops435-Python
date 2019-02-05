def h2i(obj):
    source = str(obj).lower()
    temp = '0'
    target = '0123456789abcdef'
    				 
    for c in source:
        if c in target:
           temp = temp + c
    print(temp)
    result = int(temp,16)
    return result

if __name__ == '__main__':
	print(h2i('F'))
	#print(h2i(['10','The Pond Road','Toronto']))
	