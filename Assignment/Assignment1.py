#!/usr/bin/env python3

def dbda(var1,var2):
  validate(var1)


  return result

def validate(var1):
	if len(var1) != 8:   # Check date format
		print("Wrong date format")
	else:
	    year = int(var1[0:4])
	    month = int(var1[4:6])
	    day = int(var1[6:])
	    
	    if (year % 4 == 0):
	      if (year % 100 == 0):
	        if (year % 400 ==0):
	          feb = 29
	        else:
	          feb = 28
	      else:
	        feb = 29
	    else:
	      feb = 28
	    ## Done Check Leaf year
	    

	    mon_max = { 1:31, 2:feb, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}


	    # Check month and day are valid or not
	    if month not in mon_max.keys():
	    	print("Wrong month input")
	    else:
	    	day_max = mon_max[month]
	    	if day not in range (1,day_max+1):    ### Plus 1 to take the last value
	    		print("Wrong day input")

	return mon_max

def tomorow(var1,num):
	validate(var1)
	print(mon_max)

#def yesterday(var1, num)


if __name__ == "__main__":
  var1 = '20190331'
  var2 = +3
  var3 = -3
  #dbda(var1,var2)
  #dbda(var1,var3)
  #validate(var1)
  tomorow(var1, 4)