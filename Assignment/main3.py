#!/usr/bin/env python3
'''
OPS435 Assignment 3 - Winter 2018
Program: ccn_vlha.py
Author: "Van Linh Ha"
The python code in this file ccn_vlha.py is original work written by
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





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Class Cancellation Notification System",
     epilog = "Copyright 2018 - Linh Van Ha")

    parser.add_argument('noti_site',metavar = 'N', nargs='*',help='list of notification subscription sites to be processed')
    parser.add_argument('-s', '--site', choices = ['user','host']
        ,help='generate user name or remote host IP from the given files')
    parser.add_argument('-r', '--rhost', help='usage report for the given remote host IP')
    parser.add_argument('-t', '--type', choices = ['daily','weekly','monthly']
        ,help='type of report: daily, weekly, and monthly')
    parser.add_argument('-u', '--user' ,help='usage report for the given user name')
    parser.add_argument('-v', '--verbose',metavar='',help='tune on output verbosity')
    args = parser.parse_args()

    