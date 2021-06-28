# Champernowne's constant
const = ""
k = 1
while(len(const) < 1000000):
    const += str(k)
    k += 1

ans = 1
for i in range(0, 7):
    ans *= int(const[10**i - 1])
print(ans)
