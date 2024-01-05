def no_c(my_string):
    result = ""

    for char in my_string:
        if char == 'c' or char == 'C':
            my_string.remove (char)
            result += char
return result