x = 2**1000
sum = 0

for i in range(0, len(str(x))):
    sum += int(str(x)[i])
    i += 1

print(sum)
