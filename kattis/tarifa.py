# first number is MB/month
# second is number of months
# the following are data used per month
import sys

xs = []
for line in sys.stdin:
    xs.append(line)

data = int(xs[0])
left = 0
for i in range(2, int(xs[1])+2):
    left = data - int(xs[i]) + left
print(left + data)
