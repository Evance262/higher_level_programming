#!/usr/bin/python3
for n in range(0,100):
    print("{:02d},".format(n), end=" ")
print(end='\n' if n == 99 else "")
