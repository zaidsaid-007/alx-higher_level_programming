#!/usr/bin/python3

def no_c(my_string):
    list_of_chars = list(my_string)
    new_list = [char for char in list_of_chars if char.lower() != 'c']
    return "".join(new_list)
