def s(x):
    return x / (1 - x - x ** 2)


def f(n):
    return 5 * n ** 2 + 2 * n + 1


def fib(n):
    p, c = 1, 1
    if n == 1 or n == 2:
        return 1
    for _ in range(n - 2):
        t = c
        c = p + c
        p = t
    return c


def main():
    # nth golden nugget is F(2n)*F(2n+1)
    n = 15
    gn = fib(2 * n) * fib(2 * n + 1)
    print(gn)
    return


if __name__ == "__main__":
    main()
