import sys

def knapsack(C, n, V, W):
    best = [[0 for _ in range(C+1)] for _ in range(n)]

    for i in range(n):
        for j in range(C+1):
            if i > 0:
                best[i][j] = best[i-1][j]
                if j >= W[i]:
                    best[i][j] = max(best[i-1][j-W[i]] + V[i], best[i][j])
            else:
                if j >= W[0]:
                    best[0][j] = V[0]
    return best

def knapsack_construct(C, n, V, W):
    best = knapsack(C, n, V, W)
    i = n-1
    j = C
    ans = []

    while (i > 0):
        if (j - W[i] >= 0) and (V[i] > 0) \
          and (best[i][j] == best[i-1][j - W[i]] + V[i]):
            ans.append(i)
            j -= W[i]
        i -= 1
    if (best[0][j] == V[0]) and V[0] > 0:
        ans.append(i)

    return ans

for line in sys.stdin:
    C,n = map(int, line.split())
    vs = []
    ws = []

    for _ in range(n):
        v,w = map(int, input().split())
        vs.append(v)
        ws.append(w)

    ans = knapsack_construct(C, n, vs, ws)

    print(len(ans))
    print(" ".join(map(str, ans)))
