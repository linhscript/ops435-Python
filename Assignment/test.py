import time
import os
import subprocess



if __name__ == '__main__':

    f = open('a2_test_run_2_results.txt','r')
    data = f.readlines()
    f.close()
    result = {}
    list_result = []
    for item in data:
        if item.startswith('+'):
            commands =item.replace('+ ','').strip()
            list_result = list_result.copy()            
            list_result.clear()  
        else:  
            list_result.append(item.strip())
            result[commands] = list_result


    #print(result)
    for com_test in result.keys():
        if com_test.startswith('./ur'):
            com_test = com_test.replace('./ur.py','')

            print(com_test)
