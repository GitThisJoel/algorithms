import sys
import math
largest=[2,2] # [base, exponant]
logval=2
linenr=1
curr=linenr
for line in sys.stdin:
    b,e=map(int,line.split(','))
    comp=e*math.log(b)
    if logval<comp:
        largest=[b,e]
        logval=comp
        linenr=curr
    curr+=1
print(linenr)
