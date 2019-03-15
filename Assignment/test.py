import time
import os



if __name__ == '__main__':

    f = open('a2_test_run_2_results.txt','r')
    data = f.readlines()
    f.close()
    commands = []
    result = {}
    num = 0
    list_result = []
    for item in data:
        if item.startswith('+'):
            commands.append(item[2::].strip())
            num = num + 1
            list_result.clear()
        else:
            list_result.append(item.strip())

            result[num] = list_result
            print(result)
        if num == 3:
            break 
    print(result)