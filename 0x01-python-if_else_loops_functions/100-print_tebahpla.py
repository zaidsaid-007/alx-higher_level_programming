#!/usr/bin/python3

for char_code in range(ord('z'), ord('A') - 1, -1):
    print("{}".format(chr(char_code) if char_code % 2 == 0 else chr(char_code - 32)), end="")

print()
