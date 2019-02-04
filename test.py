from datetime import date,timedelta,datetime	
test = '2019-05-23'
dt = datetime.strptime(test,"%m/%d/%y") + timedelta(35)
print(dt)