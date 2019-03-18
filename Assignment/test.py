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
            commands =item.strip()
            list_result = list_result.copy()            
            list_result.clear()  
        else:  
            list_result.append(item.strip())
            result[commands] = list_result


    #print(result)
    c = result["+ ./ur.py -l user a2_test_data_2"]
    cmd = 'python3.6 test_main.py -l user a2_test_data_2'
    #print('Test run command',test_no,':',cmd)
    p1 = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    test = p1.communicate()[0].decode('utf-8').strip('\n')    
    print(c)
    print("")
    print(test.strip().split("\r\n"))
    print(c == test.strip().split("\r\n"))