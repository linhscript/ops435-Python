import time
import os



if __name__ == '__main__':

    f = open('test_file','r')
    data = f.readlines()
    f.close()
    commands = []
    result = {}
    num = 0
    list_result = []
    for item in data:

        if item.startswith('+'):
            #commands.append(item[2::].strip())
            list_result.clear()
            num = num + 1
        else:  
            list_result.append(item.strip())
            result[num] = list_result
        if num == 3:
            break
    print(result)