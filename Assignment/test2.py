data = {'2018 02 13':1580,'2018 02 14':84657,'2018 02 15':1563}
subject = 'rchan'
text = "Daily Usage Report for "
l = len(text+str(subject))
print(text+str(subject))
print(l*'=')
print("Date"+" "*(l//2)+"Usage in Seconds")
for key in sorted(data.keys(),reverse=True):
    print(str(key) +" "*(l//2)+ str(data[key]))
print("Total" +" "*(l//2),15324)

