import sys

def scalarProd(u, v):
    prod = 0
    for i in range(len(u)):
        prod += u[i]*v[i]
    return prod

T = int(input()) # nbr of test cases
case = 1
for line in sys.stdin:
    n = int(line)
    v1 = list(map(int, input().split())); v1.sort()
    v2 = list(map(int, input().split())); v2.sort(reverse=True)

    minProd = scalarProd(v1,v2)
    print("Case #{}: {}".format(case, minProd))
    case += 1
