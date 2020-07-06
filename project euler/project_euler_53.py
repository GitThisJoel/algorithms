# nCr = n!/(r!(n-r)!), 1 <= n <= 100
# => 0 <= r < n
import math
nbrOfMillions = 0

for n in range(1, 101):
    for r in range(0, n):
        nCr = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
        if(nCr > 1000000):
            nbrOfMillions += 1
        r += 1
    n += 1

print(nbrOfMillions)
