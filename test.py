#!/usr/bin/env python3

def read_file_string(file_name):
    f = open(file_name,'r')
    file_string = f.read()
    f.close()
    return file_string

def read_file_list(file_name):
    f = open(file_name,'r')
    file_list = f.readlines()
    f.close()
    result = []
    for i in file_list:
        result.append(i.strip())
    return result

def write_file_list(file_name, list_of_lines):
    f = open(file_name, 'w')
    for num in list_of_lines:
        f.write(str(num) + '\n')
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    f = open(file_name_read, 'r')
    read_file = f.readline()
    f.close()
    print(read_file)




if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))  