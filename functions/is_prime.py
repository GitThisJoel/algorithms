def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqr = n ** 0.5
    i = 3
    while i <= sqr + 1:
        if n % i == 0:
            return False
        i += 2
    return True
