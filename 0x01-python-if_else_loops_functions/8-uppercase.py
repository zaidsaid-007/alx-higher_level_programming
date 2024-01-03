def uppercase(s):
    for char in s:
        uppercase_char = chr(ord(char) - 32) if ord(char) >= ord('a') and ord(char) <= ord('z') else char
        print("{}".format(uppercase_char), end="")
    print()

# Test cases
uppercase("best")
uppercase("Best School 98 Battery street")
