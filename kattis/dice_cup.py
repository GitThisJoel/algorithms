# input is two numbers
# print all number,including the input, between

import sys

for line in sys.stdin:
    ab = line.split(" ")
    a = int(ab[0])
    b = int(ab[1])

if(b < a):
    temp = a
    a = b
    b = temp

for i in range(a+1, b+2):
    print(i)
