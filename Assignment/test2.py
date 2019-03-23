import sys

l1 = ['a','b','c']
l2 = [1,2,3]
l2[0] = 6
#l5.split('\n')[1] = 'AAA'
result = {}
num = []
d = {'a':1,'b':2,'c':3,'d':4}



#a= list(d.values())
#print(a)
a = 0
for i in range(1,27):
   a +=i
print(a)

print(map(lambda x: x*2,list(range(1,27))))