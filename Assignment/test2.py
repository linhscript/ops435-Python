list1 = ['1','2','3']
list2 = ['a','e','c','b','h']
list3 = [1,2,3,4,5,6,7,8,'e','g','h']

tests = { 1:['20180101 1','20180102'],
         2:['20180101 -1','20171231'],
         3:['20180101 2','20180103'],
         4:['--step 20180101 3','20180102\n20180103\n20180104\n'],
         5:['20180701 500','20191113'],
         6:['20189901 2','Error: wrong month entered'],
         7:['20180199 2','Error: wrong day entered'],
         8:['2018 2','Error: wrong date entered']
        }
#new_list = list(map((lambda x:x<5),list3))

def gen():
	return (sorted(list2))
	#print(*sorted(list2),sep = "\n")

if __name__ == '__main__':

	print(gen())
