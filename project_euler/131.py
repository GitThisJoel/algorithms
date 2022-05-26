def is_prime(n):
    if n==2: 
        return True
    elif n%2==0:
        return False
    
    i = 3
    sqrn = int(n**0.5)+1
    while i < sqrn:
        if n%i==0:
            return False
        i += 2
    return True


lim = 1_000_000

cnt = 0
n = 1
diff = (n+1)**3 - n**3
while diff < lim:
    if is_prime(diff):
        cnt += 1
    n += 1
    diff = (n+1)**3 - n**3
print(cnt)
