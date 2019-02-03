#!/usr/bin/env python3
#import sys
#print(sys.version)

def validate(var1):
	mon_max = { 1:31, 2:30, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	return mon_max

def tomorow(var1, num):
	test= validate(var1)
	print(test)

#def yesterday(var1, num)


if __name__ == "__main__":
  var1 = '20190331'
  var2 = +3
  var3 = -3
  #dbda(var1,var2)
  #dbda(var1,var3)
  validate(var1)
  tomorow(var1,4)
