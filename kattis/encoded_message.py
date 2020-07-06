lines = int(input())

for _ in range(0, lines):
    out = ""
    s = input()
    side = int(len(s)**0.5)
    for i in range(side-1,-1,-1):
        for j in range(0, len(s), side):
            out += s[i+j]
    print(out)
