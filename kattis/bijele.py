# print how many chess pices that should be removed

import sys

for line in sys.stdin:
    chess = line.split(" ")

want = [1,1,2,2,2,8]
xs = []
for i in range(0, len(chess)):
    xs.append(int(chess[i]))

txt = ""
for i in range(0, len(xs)):
    txt += str(want[i] - xs[i]) + " "
print(txt)
