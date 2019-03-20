import sys
l5='user1\nuser2\nuser3'
l1 = ['a','b','c']
l2 = [1,2,3]
l2[0] = 6
l5.split('\n')[1] = 'AAA'
print(l5)
result = {}
num = []
for item in l2:
	num.append(item)
	result[1] = num
#print(l2.pop(1))

result[1].append(l1)


print('\033[91m',result,'"\033[0m"')
print( '\033[1;30mGray like Ghost\033[1;m')


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print (color.BOLD + 'Hello World !' + color.END)

print("\033[1;32;40m Bright Green  \n")

print(len(l1))

t = 'Sat Dec 30 03:25:02 2017'
print(t[0:6])

asdasd