l1 = ['a','b','c']
l2 = [1,2,3]
result = {}
num = []
for item in l2:
	num.append(item)
	result[1] = num
#print(l2.pop(1))

result[1].append(l1)


print(result)