import sys
import math

xs = []
for line in sys.stdin:
    xs.append(line)
N = xs[0]

#need to convert tX and gX to double, right now they are strings
area = 0
for i in range(1, len(xs)-1):
    val = xs[i].split(' ')
    g1 = float(val[0])
    t1 = float(val[1])

    val = xs[i+1].split(' ')
    g2 = float(val[0])
    t2 = float(val[1])

    deltaG = math.fabs(g2-g1)

    area += ((t1+t2)/2)*deltaG
print(round(area/10**3, 8))
