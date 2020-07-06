inp = input().split(" ")

N = int(inp[0])
max = (int(inp[1])**2 + int(inp[2])**2)**0.5

for _ in range(0, N):
    i = int(input())
    if(i <= max):
        print("DA")
    else:
        print("NE")
