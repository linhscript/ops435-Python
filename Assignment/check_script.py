#! /usr/bin/env python3
'''This check script will run the sample tests on assignment 1 script 
before submitting to blackboard by the students.
Please note that this script does not check the docstring of the script 
or its functions.

Released by Van Linh Ha, March 15 2019
'''

# check if user already has data file or not, if not then download it.

import types 
import sys
import os
import subprocess


def preliminary_grading(stud_name):
    message = '\n== Preliminary A2 Test Run Report for '+stud_name+'==\nThe following is your preliminary test run report for assignment 2. Please review the report and fix all the possible errors before submitting your python script and document files to blackboard using the assignment 2 submission link which will be available on Monday, February 18, 2019.\n'
    return message


if __name__ == '__main__':
    if len(sys.argv) != 2:
        student = input('Please enter your email user id:')
    else:
        student = sys.argv[1]
   
    a2_script = 'a2_'+student+'.py'
    if not os.path.isfile(a2_script):
        print('=' * 70)
        print('Your A2 script file',a2_script,'is not in the current direcoty')
        print('Please copy this script to the directory that contains your')
        print('A2 script file and run the this test run script again.')
        print('=' * 70)
        sys.exit()

    cmd_file ='wget https://scs.senecac.on.ca/~raymond.chan/ops435/a2/a2_test_data_2'
    test_file = subprocess.run(cmd_file)

    print(preliminary_grading(student))
    print('=' * 40)
    doc_marks = {} # data dictionary for documentation mark
    total_doc_marks = 0
   