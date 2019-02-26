#!/usr/bin/env python3
'''
   authorship declaration

   __author__ Linh Van Ha
   __date__ 25 Feb 2019
   __version__ 1.0
 
   text to describe the purpose of this script
'''

import os 
import sys
import time
import argparse

def get_login_rec():
    ''' docstring for this fucntion
    get records from the last command
    filter out the unwanted records
    add filtered record to list (login_recs)'''
    cmd = "last -Fiw"
    p = os.popen(cmd)  
    result = p.readlines()
    p.close() 
    login_recs = []
    for item in result:
        if len(item.split()) == 15: 
            login_recs.append(item)
    return login_recs
 
def read_login_rec(filelist):

    f = open(filelist,'r')
    login_rec = f.readlines()
    f.close()
    return login_rec

def get_list (list_record,position):
    res_list = set()
    for item in list_record:
        res_list.add(item.split()[position])

    #for i in sorted(res_list):
    #   print(i)
    print(*sorted(res_list),sep = "\n")

def format_record(unformat_record):

    record_list = []
    for item in unformat_record:
        time1 = time.strptime(' '.join(item.split()[3:8]),"%a %b %d %H:%M:%S %Y")
        time2 = time.strptime(' '.join(item.split()[9:14]),"%a %b %d %H:%M:%S %Y")
        # time1 and time2 is struct_time
        doy1 = time.strftime("%j",time1) # return day of year
        doy2 = time.strftime("%j",time2)
 
        if doy1 == doy2: # if same day
            record_list.append(item.split()) # save the record to list
        else: # this works even jump to many days
            next_day = time.mktime(time1) # float number
            
            eod_time = time.ctime(next_day).split() #convert to readable time
            old_day = item.split()

            old_day[9] = eod_time[0]
            old_day[10] = eod_time[1]
            old_day[11] = eod_time[2]
            old_day[12] = '23:59:59'
            old_day[13] = eod_time[4]                           
            record_list.append(old_day)
            while doy1 != doy2:
                                
                next_day = next_day + 86400 #floating number
                new_day = item.split()
                new_time = time.ctime(next_day).split() # covert to readable time
                new_day[3] = new_time[0]
                new_day[4] = new_time[1]
                new_day[5] = new_time[2]
                new_day[6] = '00:00:00'
                new_day[7] = new_time[4]
                doy1 = time.strftime('%j',time.localtime(next_day))

                if doy1 != doy2: # check if next day is on the same day with end day or not
                    new_day[9] = new_time[0]
                    new_day[10] = new_time[1]
                    new_day[11] = new_time[2]
                    new_day[12] = '23:59:59'
                    new_day[13] = new_time[4]
                record_list.append(new_day)
    return record_list

def cal_daily_usage(subject,login_recs):
    ''' docstring for this function
    generate daily usage report for the given 
    subject (user or remote host)'''
    text = "Daily Usage Report for "
    l = len(text+str(subject))
    print(text+str(subject))
    print(l*'=')
    print("Date"+" "*(l//2)+"Usage in Seconds")
    total = 0
    daily_usage = {}
    for value in login_recs:
        if subject in value:
            time_usage = int(time.mktime(time.strptime(' '.join(value[9:14]))) - time.mktime(time.strptime(' '.join(value[3:8]))))
            time_format = time.strftime('%Y %m %d',time.strptime(' '.join(value[9:14])))
            try:
                daily_usage[time_format] += time_usage
            except:
                daily_usage[time_format] = time_usage
            total += time_usage

    for key in sorted(daily_usage.keys(),reverse=True):
        print(str(key) +" "*(l//2)+ str(daily_usage[key]))
    print("Total" +" "*(l//2),total)
    
def cal_weekly_usage(subject,login_recs):
    ''' docstring for this function
    generate weekly usage report for the given 
    subject (user or remote host)'''
    text = "Weekly Usage Report for "
    l = len(text+str(subject))
    print(text+str(subject))
    print(l*'=')
    print("Week #"+" "*(l//2)+"Usage in Seconds")
    total = 0
    weekly_usage = {}
    for value in login_recs:
        if subject in value:
            time_usage = int(time.mktime(time.strptime(' '.join(value[9:14]))) - time.mktime(time.strptime(' '.join(value[3:8]))))
            time_format = time.strftime('%Y %W',time.strptime(' '.join(value[9:14])))
            try:
                weekly_usage[time_format] += time_usage
            except:
                weekly_usage[time_format] = time_usage
            total += time_usage

    for key in sorted(weekly_usage.keys(),reverse=True):
        print(str(key) +" "*(l//2)+ str(weekly_usage[key]))
    print("Total" +" "*(l//2),total)

def cal_monthly_usage(subject,login_recs):
    ''' docstring for this function
    generate monthly usage report fro the given
    subject (user or remote host)'''
    text = "Monthly Usage Report for "
    l = len(text+str(subject))
    print(text+str(subject))
    print(l*'=')
    print("Month"+" "*(l//2)+"Usage in Seconds")
    total = 0
    monthly_usage = {}
    for value in login_recs:
        if subject in value:
            time_usage = int(time.mktime(time.strptime(' '.join(value[9:14]))) - time.mktime(time.strptime(' '.join(value[3:8]))))
            time_format = time.strftime('%Y %m',time.strptime(' '.join(value[9:14])))
            try:
                monthly_usage[time_format] += time_usage
            except:
                monthly_usage[time_format] = time_usage
            total += time_usage

    for key in sorted(monthly_usage.keys(),reverse=True):
        print(str(key) +" "*(l//2)+ str(monthly_usage[key]))
    print("Total" +" "*(l//2),total)
     
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Usage Report based on the last command",
     epilog = "Copyright 2018 - Linh Van Ha")

    parser.add_argument('filename',metavar = 'F', nargs='*',help='list of files to be processed')
    parser.add_argument('-l', '--list', choices = ['user','host']
        ,help='generate user name or remote host IP from the given files')
    parser.add_argument('-r', '--rhost', help='usage report for the given remote host IP')
    parser.add_argument('-t', '--type', choices = ['daily','weekly','monthly']
        ,help='type of report: daily, weekly, and monthly')
    parser.add_argument('-u', '--user' ,help='usage report for the given user name')
    parser.add_argument('-v', '--verbose',metavar='',help='tune on output verbosity')
    args = parser.parse_args()

###################################################################
    login_rec = []
    for file in args.filename:
        login_rec.extend(read_login_rec(file))

    if args.list:
        if args.list == 'user':
            number = 0
        else:
            number = 2
        get_list(login_rec,number)
    

###################################################################

    if args.rhost:
        subject = args.rhost
    elif args.user:
        subject = args.user

    if args.type:
        record_list = format_record(login_rec)
        if args.type == 'daily':
            cal_daily_usage(subject,record_list)
        elif args.type == 'weekly':
            cal_weekly_usage(subject,record_list)
        else:
            cal_monthly_usage(subject,record_list)

'''
Files to be processed: ['a2_test_data_0']
Type of args for files <class 'list'>
processing usage report for the following:
reading login/logout record files ['a2_test_data_0']
Generating list for user
'''