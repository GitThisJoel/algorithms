import math
ps=[2,3,5]
def next_prime():
    s=ps[-1]+2
    while True:
        mp=s
        for p in ps:
            while mp%p==0:
                mp//=p
        if mp==s:
            ps.append(s)
            return s
        s+=1
r=0
n=4
while r<10**10:
    p=next_prime()
    r=((p-1)**n+(p+1)**n)%(p**2)
    n+=1
print(n-1)
