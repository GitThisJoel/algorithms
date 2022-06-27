prices = list(map(float, input().split()))

# assert list longer than 2
lo = prices[0]
d1 = 1
d2 = -1
best = -99999999999999999999999999

for i, p in enumerate(prices[1:]):
    i += 2
    if p < lo:
        lo = p
        d1 = i
    elif (p-lo) > best:
        best = p-lo
        d2 = i

print(f"best day to buy is {d1} and best day to sell is {d2}, profit = {best}")
