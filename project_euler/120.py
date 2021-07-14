rsum=0
for a in range(3,1001):
    rs=set()
    n=1
    r=-1
    while not r in rs:
        rs.add(r)
        r=((a-1)**n+(a+1)**n)%(a**2)
        n+=2
    rs.remove(-1)
    rsum+=max(rs)
print(rsum)
