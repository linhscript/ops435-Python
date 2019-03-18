import time
import os



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


    print(result)