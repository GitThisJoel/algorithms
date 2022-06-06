# 5 <= p1 <= 10**6
import math


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


def next_prime(p):  # assume p is prime
    p += 2
    while not is_prime(p):
        p += 2
    return p


def digs(x):
    return math.ceil(math.log(x, 10))


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def extended_gcd(a, b):
    s = 0
    old_s = 1
    r = b
    old_r = a

    while not r == 0:
        q = old_r // r
        old_r, r = r, (old_r - q * r)
        old_s, s = s, (old_s - q * s)

    # if not b == 0:
    #     bezout_t = (old_r - old_s * a) // b
    # else:
    #     bezout_t = 0

    # print("Bézout coefficients:", (old_s, bezout_t))
    # print("greatest common divisor:", old_r)
    return old_s


def find_n(p1, p2):
    a = 10 ** digs(p1)
    b = p2 - p1
    m = p2

    d = gcd(a, m)
    x = extended_gcd(a, m)

    x0 = b * x * d % m

    return a * x0 + p1


def main():
    p1 = 5
    p2 = next_prime(p1)
    p1_lim = 10 ** 6
    S = 0
    while p1 <= p1_lim:
        temp_S = find_n(p1, p2)
        S += temp_S
        # print(f"{p1=}, {p2=}, with {temp_S=}, now {S=}")
        p1 = p2
        p2 = next_prime(p1)
    print(S)
    return S


if __name__ == "__main__":
    main()
