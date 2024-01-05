def replace_in_list(my_list,idx,element):
    new_list=my_list[2]==7

    listlength = len(my_list)-1

    if idx<0 and idx> listlength:
        return my_list
    else:
        my_list[idx] = element

    return my_list  


