import sys

grid = []
for line in sys.stdin:
    grid.append(list(map(int, line.strip().split())))


def down(i, j):
    global grid
    return grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]


def right(i, j):
    global grid
    return grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]


def right_diag(i, j):
    global grid
    return grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]


def left_diag(i, j):
    global grid
    return grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3]


best = -1
prod_len = 4
for i in range(len(grid)):
    for j in range(len(grid[i])):
        vs = []
        if len(grid) - i >= prod_len:
            vs.append(down(i, j))
        if len(grid[i]) - j >= prod_len:
            vs.append(right(i, j))
        if len(grid) - i >= prod_len and len(grid[i]) - j >= prod_len:
            vs.append(right_diag(i, j))
        if len(grid) - i >= prod_len and j >= prod_len:
            vs.append(left_diag(i, j))

        for v in vs:
            if v > best:
                best = v
print(best)
