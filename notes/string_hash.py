# does the string T contain S

# naive solution
def naive_contains(S, T):
    for i in range(len(T) - len(S)+1):
        ok = True
        for j in range(len(S)):
            if S[i] != T[j]:
                ok = False
                break
        if ok:
            return True
    return False

# better way
MOD = 10**16 + 61

def pre_hash(S):
    su = 0
    for ch in S:
        su = (su*128 + ord(ch)) % MOD
    return su

def contains(S, T):
    v = pre_hash(S)
    v2 = pre_hash(T[:len(S)])
    pw = pow(128, len(S) - 1, MOD)

    for i in range(len(T) - len(S)):
        if v == v2:
            return True
        # rm = int(T[i])*128**(len(S)-1)
        rm = ord(T[i]) * pw
        add = ord(T[i+len(S)])
        v2 = ((v2 - rm)*128 + add) % MOD
    return v == v2

print(contains('11', '2222222222211'))

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    Limit = int(n**.5) + 3
    for i in range(3, Limit, 2):
        if n%i == 0:
            return False
    return True

# get new random prime number
import random
def find_new_prime():
    Start = random.randint(10**16, 10**17)
    while not is_prime(Start):
        Start += 1
    print(start)
