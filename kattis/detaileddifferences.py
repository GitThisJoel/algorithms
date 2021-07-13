n=int(input())
for _ in range(n):
    out=''
    xs=input().strip()
    ys=input().strip()
    for i in range(len(xs)):
        if xs[i]==ys[i]:
            out+='.'
        else:
            out+='*'
    print(xs)
    print(ys)
    print(out)
    print()
