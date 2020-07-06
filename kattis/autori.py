# create a word with the starting letter of all input

import sys

res = ""
name = []
for line in sys.stdin:
    name = line.split('-')
for i in range(0, len(name)):
    res += name[i][0]
print(res)
