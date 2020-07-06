import  sys

xs = []
for line in sys.stdin:
    xs.append(line)

for i in range(0, len(xs)):
    s = xs[i].split(" ")
    ab = abs(int(s[0])-int(s[1]))
    print(ab)
