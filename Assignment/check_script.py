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

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def preliminary_grading(stud_name):
    message = '\n== Preliminary A2 Test Run Report for '+stud_name+'==\nThe following is your preliminary test run report for assignment 2. Please review the report and fix all the possible errors before submitting your python script and document files to blackboard using the assignment 2 submission link which will be available on Monday, February 18, 2019.\n'
    return message


if __name__ == '__main__':
    if len(sys.argv) != 3:
        student = input('Please enter your email user id:')
        fullname = input('Please enter your FULL NAME:')
    else:
        student = sys.argv[1]
        fullname = sys.argv[2]
   
    a2_script = 'a2_'+student+'.py'
    if not os.path.isfile(a2_script):
        print('=' * 70)
        print('Your A2 script file',a2_script,'is not in the current direcoty')
        print('Please copy this script to the directory that contains your')
        print('A2 script file and run the this test run script again.')
        print('=' * 70)
        sys.exit()

    if not os.path.isfile("a2_test_run_2_results.txt"):
        cmd_file ='wget https://scs.senecac.on.ca/~raymond.chan/ops435/a2/a2_test_run_2_results.txt'
        os.system(cmd_file)

    print(preliminary_grading(student))
    print('=' * 40)
    doc_marks = {} # data dictionary for documentation mark
    total_doc_marks = 0

    f = open('a2_test_run_2_results.txt','r')
    data = f.readlines()
    f.close()
    tests = {}
    list_coms = []
    for item in data:
        if item.startswith('+'):
            commands = item.replace('+ ','').strip()
            list_coms = list_coms.copy()            
            list_coms.clear()  
        else:
            if item.endswith("Chan\n"):
                item = item.replace('Raymond Chan',fullname)
            if item.startswith("usage"):
                item = item.replace('ur','a2_'+student)            
            list_coms.append(item.rstrip())
            tests[commands] = list_coms
            break
    test_marks = {}
    num = 1
    for com_test in tests.keys():
        if com_test.startswith('./ur'):
            expected = '\n'.join(tests[com_test])
            com_test = com_test.replace('./ur.py','')
            cmd = 'python3.6 a2_'+student+'.py'+ com_test
            print('Test run command',':',cmd)
            p1 = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            result = p1.communicate()[0].decode('utf-8').strip('\n')
              
            if result == expected:
                print(color.GREEN,'--test passed--',color.END)
                test_marks[num] = 1
            else:

                print(color.RED,color.BOLD,'--test failed--',color.END)
                print(color.BLUE,color.UNDERLINE,'---- expect:',color.END,expected)
                print(color.BLUE,color.UNDERLINE,'----  given:',color.END,result)
                test_marks[num] = 0


            num +=1

    print('Test Results:',test_marks)
    total_test_marks = 0
    for item in test_marks:
        total_test_marks += test_marks[item] 
    total_test_marks = total_test_marks / 17 * 100 ## 17 commands to check
    print('Total test run marks: ',total_test_marks)
    grand_total = round((total_test_marks + total_doc_marks),2)
    print('Total marks for script (max. 100):',color.UNDERLINE,color.YELLOW,grand_total,color.END) 
    a=expected.split('\n')
    print(a)
    print("")
    b=result.split('\n')
    print(b)
 