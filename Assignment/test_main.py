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
    '''
    '''
    f = open(filelist,'r')
    login_recs = f.readlines()
    f.close()
    return login_recs

def get_list (list_record,position):
    
    res_list = set()
    for item in list_record:
        res_list.add(item.split()[position])
    return res_list

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

    return daily_usage,total
    
def cal_weekly_usage(subject,login_recs):
    ''' docstring for this function
    generate weekly usage report for the given 
    subject (user or remote host)'''
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
    return weekly_usage,total

def cal_monthly_usage(subject,login_recs):
    ''' docstring for this function
    generate monthly usage report fro the given
    subject (user or remote host)'''
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
    return monthly_usage,total

def content(calculation):
    ft = []
    records,total = calculation
    for key in sorted(records.keys(),reverse=True):
        ft.append("{:<11s}{:>11d}".format(str(key),records[key]))
    ft.append("{:<11s}{:>11d}".format("Total",total))
    return ft

def gen_text(): 
    text = []
    text.append("Files to be processed: "+ str(args.filename))
    text.append("Type of args for files "+ str(type(args.filename)))

    if args.list: 
        text.append("processing usage report for the following: ")
        text.append("reading login/logout record files "+ str(args.filename))
        text.append("Generating list for "+ str(args.list))
    else: 
        text.append("usage report for user: "+ str(subject))
        text.append("usage report type: " + str(args.type))
        text.append("processing usage report for the following: ")
        text.append("reading login/logout record files "+ str(args.filename))
    return text

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Usage Report based on the last command",
     epilog = "Copyright 2018 - Linh Van Ha")

    parser.add_argument('filename',metavar = 'F', nargs='+',help='list of files to be processed')
    parser.add_argument('-l', '--list', choices = ['user','host']
        ,help='generate user name or remote host IP from the given files')
    parser.add_argument('-r', '--rhost', help='usage report for the given remote host IP')
    parser.add_argument('-t', '--type', choices = ['daily','weekly','monthly']
        ,help='type of report: daily, weekly, and monthly')
    parser.add_argument('-u', '--user' ,help='usage report for the given user name')
    parser.add_argument('-v', '--verbose',action="store_true",help='tune on output verbosity')
    args = parser.parse_args()

###################################################################
    print(args.filename)
    unformatted_login_rec = []
    if "last" in args.filename:
        unformatted_login_rec.extend(get_login_rec())
    else:
        for file in args.filename:
            unformatted_login_rec.extend(read_login_rec(file))

    if args.rhost:
        subject = args.rhost
    elif args.user:
        subject = args.user

    if args.verbose:
        print(*gen_text(),sep="\n")

    if args.list:
        if args.list == 'user':
            position = 0
        else:
            position = 2
        print(str(args.list).title() + " list for", ' '.join(args.filename))
        print(len(str(args.list).title() + " list for "+ ' '.join(args.filename))*'=')
        print(*sorted(get_list(unformatted_login_rec,position)),sep = "\n")
    
    elif args.type:
        record_list = format_record(unformatted_login_rec)
        print(args.type.title() + " Usage Report for " + subject)
        print(len(args.type.title() + " Usage Report for " + subject)*'=')
        if args.type == 'daily':
            print("{:<14s}{:>14s}".format("Date","Usage in Seconds"))
            print(*content(cal_daily_usage(subject,record_list)),sep = "\n")
        elif args.type == 'weekly':
            print("{:<14s}{:>14s}".format("Week #","Usage in Seconds"))
            print(*content(cal_weekly_usage(subject,record_list)),sep = "\n")
        else:
            print("{:<14s}{:>14s}".format("Month","Usage in Seconds"))
            print(*content(cal_monthly_usage(subject,record_list)),sep = "\n")
