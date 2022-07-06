from random import randint


def shuffle(a):
    for i in range(len(a) - 1, 1, -1):
        j = randint(0, i)
        t = a[i]
        a[i] = a[j]
        a[j] = t
    return a
