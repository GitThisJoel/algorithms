def climbStairs(n: int) -> int:
    prev = 1
    curr = 1
    if n == 1:
        return 1

    for i in range(n-1):
        temp = curr
        curr = prev + curr
        prev = temp
    return curr

climbStairs(2)
