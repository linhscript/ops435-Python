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



cmd1 = grep td filename
cmd2 = sed  -i 's/<td>//g ;s/<\/td>//g'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Class Cancellation Notification System",
     epilog = "Copyright 2018 - Linh Van Ha")

    parser.add_argument('noti_site',metavar = 'N', nargs='*',help='list of notification subscription sites to be processed')
    parser.add_argument('-s', '--site', default='https://scs.senecac.on.ca/~raymond.chan/ops435/a3/ccn.html', help='class cancellation web site')
    parser.add_argument('-t', '--type', choices = ['table','text']
        ,help='type of class concellation data: table -> html table,text -> plain text file')
    parser.add_argument('-n', '--notification ', choices = ['table','text']
        ,help='type of notification data: table -> html table, text-> plain text file')
    args = parser.parse_args()

    
    
    

