inp = input().split(" ")
b = int(inp[0])
d = int(inp[1])
c = int(inp[2])
l = int(inp[3])
count = 0

for i in range(0, int(l/b)+1):
    for j in range(0, int(l/d)+1):
        for k in range(0, int(l/c)+1):
            if(i*b+j*d+k*c == l):
                print(str(i) + " " + str(j) + " " + str(k) + "\n")
                count += 1

if(count == 0):
    print("impossible")
