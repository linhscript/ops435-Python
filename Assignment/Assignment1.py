#!/usr/bin/env python3

def dbda(var1,var2):
  validate(var1)


  return result

def validate(var1):
  if len(var1) != 8:   # Check date format
    print("Wrong date format ")
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
    


    


  return 

def tomorow(var1, num):
  return

def yesterday(var1, num)


if __name__ == "__main__":
  var1 = 20190315
  var2 = +3
  var3 = -3
  dbda(var1,var2)
  dbda(var1,var3)