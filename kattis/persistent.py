import sys
import math
for s in sys.stdin:
    s = s.strip()
    x = int(s)
    if x==-1:
        exit(0)
    elif len(s)==1:
        print('1'+s)
    else:
        factors=[]
        for i in range(9,1,-1):
            while x%i==0:
                factors.append(str(i))
                x//=i
        if x>=10:
            print("There is no such number.")
            continue
        else:
            factors.sort()
            print(''.join(factors))
