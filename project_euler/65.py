# Convergents of e 

xs = []
index = 1

for i in range(0, 100):
    if(((i + 2) % 3) == 0):
        xs.append(2*index)
        index += 1
    else:
        xs.append(1)
    i += 1

t = []
t.append(2)
t.append(1)
t.append(8)
t.append(11)

for j in range(4, 100):
    t.append(t[j - 1]*xs[j-1] + t[j - 2])

sum = 0
for i in range(0, len(str(t[99]))):
    sum += int(str(t[99])[i])
    i += 1

print(sum)
