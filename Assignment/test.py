import time
import os
import subprocess



if __name__ == '__main__':

    f = open('a2_test_run_2_results.txt','r')
    data = f.readlines()
    f.close()
    tests = {}
    list_coms = []
    for item in data:
        if item.startswith('+'):
            commands =item.replace('+ ','').strip()
            list_coms = list_coms.copy()            
            list_coms.clear()  
        else:  
            list_coms.append(item.strip())
            tests[commands] = list_coms
    test_marks = {}
    for com_test in tests.key():
        if com_test.startswith('./ur'):
            com_test.replace('./ur', student)

            cmd = 'python3 a2_'+student+'.py '+ com_test
            print('Test run command',test_no,':',cmd)
            p1 = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            result = p1.communicate()[0].decode('utf-8').strip('\n')  
            expected = test.split("\n")
            if result == expected:
                print('--test passed--')
                test_marks[test_no] = 1
            else:
                print('--test failed--')
                print('---- expect:',expected)
                print('----  given:',result)
                test_marks[test_no] = 0

    print('Test Results:',test_marks)
    total_test_marks = 0
    for item in test_marks:
    total_test_marks += test_marks[item] 
    total_test_marks = total_test_marks / 19 * 46
    print('Total test run marks: ',total_test_marks)
    grand_total = total_test_marks + total_doc_marks
    print('Total marks for script (max. 46):',grand_total)  
