# Implementation of Diviable Range Problem 
import math 

k = int(input())

def is_prime(n):
    if n == 2: return True # I do not really like this case...
    elif n%2 == 0: return False

    i = 3
    lim = int(n**0.5)+1
    while i < lim:
        if n%i == 0:
            return False
        i += 2
    return True

num = 1
for n in range(2,k+1):
    if is_prime(n):
        num *= n**int(math.log(k, n))

print(f"for {k=} we have:\n{num}")
