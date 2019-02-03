#!/usr/bin/env python3
#import sys
#print(sys.version)

def validate(var1):
	if (len(var1) != 8):   # Check date format
		print("Wrong date format")
	else:
		mon_max = { 1:31, 2:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
		print("Wrong day input")
	return mon_max


if __name__ == "__main__":
  var1 = '201903311'
  var2 = +3
  var3 = -3
  #dbda(var1,var2)
  #dbda(var1,var3)
  validate(var1)

