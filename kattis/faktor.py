# Find the minimal amout of scientist to bribe
# input is A, amout of articles, and I the desired factor
# I = citations / A

import sys

xs = []
A = 0; I = 0; C = 0
for line in sys.stdin:
    ai = line.split(" ")
    A = int(ai[0])
    I = int(ai[1])

C = (I-1)*A + 1
print(C)
