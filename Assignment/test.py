#!/usr/bin/env python3
'''
OPS435 Assignment 2 - Winter 2018
Program: ur_vlha.py
Author: "Van Linh Ha"
The python code in this file ur_vlha.py is original work written by
"Van Linh Ha". No code in this file is copied from any other source 
including any person, textbook, or on-line resource except those provided
by the course instructor. I have not shared this python file with anyone
or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and violators 
will be reported and appropriate action will be taken.
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
    login_recs = f.readlines()
    f.close()
    return login_recs

def get_list (list_record,position):
    gen_text()
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
    gen_text()
    text = "Daily Usage Report for "
    print(text+str(subject))
    print(len(text+str(subject))*'=')
    print("{:<14s}{:>14s}".format("Date","Usage in Seconds"))
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
        print ("{:<11s}{:>11d}".format(str(key),daily_usage[key]))
    print("{:<11s}{:>11d}".format("Total",total))
    
def cal_weekly_usage(subject,login_recs):
    ''' docstring for this function
    generate weekly usage report for the given 
    subject (user or remote host)'''
    gen_text()
    text = "Weekly Usage Report for "
    print(text+str(subject))
    print(len(text+str(subject))*'=')
    print("{:<14s}{:>14s}".format("Week #","Usage in Seconds"))
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
        print ("{:<11s}{:>11d}".format(str(key),weekly_usage[key]))
    print("{:<11s}{:>11d}".format("Total",total))

def cal_monthly_usage(subject,login_recs):
    ''' docstring for this function
    generate monthly usage report fro the given
    subject (user or remote host)'''
    gen_text()
    text = "Monthly Usage Report for "
    print(text+str(subject))
    print(len(text+str(subject))*'=')
    print("{:<14s}{:>14s}".format("Month","Usage in Seconds"))
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
        print ("{:<11s}{:>11d}".format(str(key),monthly_usage[key]))
    print("{:<11s}{:>11d}".format("Total",total))

def gen_text():
    if args.verbose:
        print("Files to be processed:",args.filename)
        print("Type of args for files",type(args.filename))

        if args.list:
            print("processing usage report for the following:")
            print("reading login/logout record files",args.filename)
            print("Generating list for",args.list)
        else:
            print("usage report for user:",subject)
            print("usage report type:",args.type)
            print("processing usage report for the following:")
            print("reading login/logout record files",args.filename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Usage Report based on the last command",
     epilog = "Copyright 2018 - Linh Van Ha")

    parser.add_argument('filename',metavar = 'F', nargs='*',default='empty',help='list of files to be processed')
    parser.add_argument('-l', '--list', choices = ['user','host']
        ,help='generate user name or remote host IP from the given files')
    parser.add_argument('-r', '--rhost', help='usage report for the given remote host IP')
    parser.add_argument('-t', '--type', choices = ['daily','weekly','monthly']
        ,help='type of report: daily, weekly, and monthly')
    parser.add_argument('-u', '--user' ,help='usage report for the given user name')
    parser.add_argument('-v', '--verbose',action="store_true",help='tune on output verbosity')
    args = parser.parse_args()

###################################################################
    unformatted_login_rec = []
    if args.filename == "empty":
        unformatted_login_rec.extend(get_login_rec())
    else:
        for file in args.filename:
            unformatted_login_rec.extend(read_login_rec(file))

    if args.list:
        if args.list == 'user':
            position = 0
        else:
            position = 2
        get_list(unformatted_login_rec,position)
    
    else:
        if args.rhost:
            subject = args.rhost
        elif args.user:
            subject = args.user

        if args.type:
            record_list = format_record(unformatted_login_rec)
            if args.type == 'daily':
                cal_daily_usage(subject,record_list)
            elif args.type == 'weekly':
                cal_weekly_usage(subject,record_list)
            else:
                cal_monthly_usage(subject,record_list)