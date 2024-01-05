#!/usr/bin/python3
def element_at(my_list,idx):
    listlength=len(my_list) - 1    

if (idx<0 or idx>=listlength):
    print("None")
else:
    print("Element at index {:d} is {}".format(my_list[idx]))

