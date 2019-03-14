from typing import List, Any

list1 = ['1','2','3']
list2 = ['a','e','c','b','h']
list3 = [1,2,3,4,5,6,7,8,'e','g','h']
text = []


def gen():
    text = []
    if 1 == 1:
        text.append("Files to be processed: " + str(file1))
        text.append("Files to be processed: " + str(file1))
        text.append("Type of args for files " + str(file1))

        if 1 == 1:
            text.append("processing usage report for the following:")
            text.append("reading login/logout record files " + str(file1))
            text.append("Generating list for " + str(file1))
        else:
            text.append("usage report for user: " + str(file1))
            text.append("usage report type: " + str(file1))
            text.append("processing usage report for the following:")
            text.append("reading login/logout record files " + str(file1))
    return text

if __name__ == '__main__':
    file1= "text1"
    file2 = "text2"
    file3 = "text3"
    print(gen())