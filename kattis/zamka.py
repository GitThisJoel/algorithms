# first line is L, second is D and third is X
# L is lower limit and D i upper, X is sum of digits
# find max and min number with satisfy

import sys
xs = []
for line in sys.stdin:
    xs.append(line)

L = int(xs[0]); D = int(xs[1]); X = int(xs[2])

def digiSum(x):
    sum = 0
    for i in range(0, len(str(x))):
        sum += int(str(x)[i])
    return sum

ans = []
for i in range(L, D+1):
    sum = digiSum(i)
    if(sum == X):
        ans.append(i)

temp = sorted(ans)
print(temp[0])
print(temp[len(temp)-1])
