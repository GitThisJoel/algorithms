den = int(input())
s = input().split(" ")
sum = 0

for i in range(0, len(s)):
    temp = int(s[i])
    if(temp >= 0):
        sum += temp
    else:
        den -= 1

frac = sum/den
print(frac)
