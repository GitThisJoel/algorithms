def is_square(x):
    if x <= 0:
        return False
    sqrt_x = x ** 0.5
    return sqrt_x == int(sqrt_x)


def min_xyz():
    found = False
    i = 4
    while not found:
        a = i * i
        for j in range(3, i):
            c = j * j
            f = a - c
            if is_square(f):
                start = 1 if j % 2 == 1 else 2
                for k in range(start, j, 2):
                    d = k * k
                    e = a - d
                    b = c - e

                    if is_square(e) and is_square(b):
                        # print(f"{a=},{b=},{c=},{d=},{e=},{f=}")
                        found = True
                        x = (a + b) / 2
                        y = (e + f) / 2
                        z = (c - d) / 2
                        return x, y, z
        i += 1


if __name__ == "__main__":
    x, y, z = min_xyz()
    s = x + y + z
    print(f"x+y+z={x}+{y}+{z}={s}")
