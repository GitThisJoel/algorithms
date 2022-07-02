xys = [
    (0, -1),
    (0, 1),
    (2, -7),
    (2, 7),
    (-4, 5),
    (-4, -5),
    (-3, 2),
    (-3, -2),
]


def p1(xn, yn):
    return -9 * xn - 4 * yn - 14, -20 * xn - 9 * yn - 28


def s(x):
    return x / (1 - x - x ** 2)


def rt(n):
    return (5 * n ** 2 + 14 * n + 1) ** 0.5


def Ag(n):
    p, c = 1, 4
    if n == 1:
        return p
    elif n == 2:
        return c
    else:
        for _ in range(n - 2):
            t = c
            c = p + c
            p = t
        return c


def main():
    nugs = set()
    for x, y in xys:
        for _ in range(30):
            x, y = p1(x, y)
            if x > 0 and x not in nugs:
                nugs.add(x)
    ns = list(nugs)
    ns.sort()
    res = sum(ns[:30])
    print(res)


if __name__ == "__main__":
    main()
