import sys

xs = []
for line in sys.stdin:
    xs.append(line)

n = int(xs[0])
a = 3
if(n==1):
    print(a**2)
else:
    for i in range(2,n+1):
        a += 2**(i-1)
    print(a**2)
