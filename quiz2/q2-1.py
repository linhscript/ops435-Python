#!/usr/bin/env python3
'''Name: Van Linh Ha - vlha
'''
def average (in_list):
    avg = 0
    total = 0
    for i in in_list:
        total += i
    avg = total/len(in_list)
    return avg

if __name__ == '__main__':
    a_list = [40,3,4,12,11]
    print('Average of',a_list,'is',average(a_list))    
    b_list = [20, 5, 2, 6, 2]
    print('Average of',b_list,'is',average(b_list))
    c_list = [11, 21, 31]
    print('Average of',c_list,'is',average(c_list))