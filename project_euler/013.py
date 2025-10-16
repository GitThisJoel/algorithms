import json
f = open('data/pe13Nbr.txt', 'r')
g = f.read().split("\n")[:-1]
sum = 0

print(g)
for i in range(0, len(g)):
    sum += int(g[i])
print(str(sum)[:10])


# "".join(f.read().split("\n"))
