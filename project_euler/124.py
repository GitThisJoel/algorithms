primes=[2]
def is_prime(x):
    if x%2==0:
        return False
    for i in range(3,int(x**0.5)+1,2):
        if x%i==0:
            return False
    return True

def rad(n):
    global primes
    if is_prime(n):
        primes.append(n)
        return n
    r=1
    for p in primes:
        t=n
        if n%p==0:
            r*=p
    return r

if __name__ == "__main__":
    rads=[(1,1),(2,2)]
    wanted=10000-1
    for i in range(3,100001):
        rads.append((i,rad(i)))
    sorted_rads=sorted(rads, key=lambda t: t[1])
    print(sorted_rads[wanted])
