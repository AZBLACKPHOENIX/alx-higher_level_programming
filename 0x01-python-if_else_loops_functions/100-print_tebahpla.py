#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -2):
    print(chr(i), end="")
    if i > ord('B'):
        print(chr(i - 32), end="")
print()
