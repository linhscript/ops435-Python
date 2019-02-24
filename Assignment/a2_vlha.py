#!/usr/bin/env python3
'''
   authorship declaration

   __author__ Linh Van Ha
   __date__ Feb 2019
   __version__ 1.0
 
   text to describe the purpose of this script
'''

import os 
import sys
import time

def get_login_rec():
    ''' docstring for this fucntion
    get records from the last command
    filter out the unwanted records
    add filtered record to list (login_recs)'''
    [ put your python code for this function here ]
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

def cal_daily_usage(subject,login_recs):
    ''' docstring for this function
    generate daily usage report for the given 
    subject (user or remote host)'''
    text = "Daily Usage Report for "
    print(text+str(subject))
    print(len(text+str(subject))*'=')
    print("Date"+" "*10+"Usage in Seconds")
    
    return daily_usage

def cal_weekly_usage(subject,login_recs):
    ''' docstring for this function
    generate weekly usage report for the given 
    subject (user or remote host)'''
    [ put your python code for this function here ]
    return weekly_usage

def cal_monthly_usage(subject,login_recs):
    ''' docstring for this function
    generate monthly usage report fro the given
    subject (user or remote host)'''
    [ put your python code for this function here ]
    return monthly_usage
     
if __name__ == '__main__':
    import argparse
    filename = 'usage_data_file'
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

    if args.type == 'daily':
        cal_daily_usage(subject,)
    elif args.type == 'weekly':
        cal_weekly_usage(subject,)
    else:
        cal_monthly_usage(subject,)