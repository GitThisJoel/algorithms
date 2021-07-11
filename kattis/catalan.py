from math import factorial as f
q=int(input())
for _ in range(q):
    n=int(input())
    cat=f(2*n)//(f(n)*f(n+1))
    print(cat)
