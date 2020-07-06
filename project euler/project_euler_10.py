# Find sum of all primes below 2 000 000
import math
sum = 2

def isPrime( nbr ):
    result = True
    sqrt = int(math.sqrt(nbr))
    for i in range(2, sqrt+1):
        if(result and nbr % i == 0):
            result = False
        i += 1
    return result

for j in range(3, 2000000): # 3 -> 1999999 
    if(isPrime(j)):
        sum += j
    j += 2

print(sum)
