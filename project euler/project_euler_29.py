# 2 <= a <= 100 & 2 <= b <= 100
# How many distinct terms of a**b

unique = set()

for a in range(2, 101):
    for b in range(2, 101):
        unique.add(a**b)
print(str(len(unique)))

#out: 9183
