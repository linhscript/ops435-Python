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
    ''' docstring for this function
    get records from given filelist
    open and read each file from the filelist
    filter out the unwanted records
    add filtered record to list (login_recs)''' 
    [ put your python code for this function here ]
    return login_rec

def cal_daily_usage(subject,login_recs):
    ''' docstring for this function
    generate daily usage report for the given 
    subject (user or remote host)'''
    [ put your python code for this function here ]
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
    ...
    [ code to retrieve command line argument using the argparse module [
    ...
    [ based on the command line option, generate and print
      the requested usage report ]
    ...