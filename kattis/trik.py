s = input()
pos = 1
for i in range(0, len(s)):
    if(s[i] == "A"):
        if(pos == 1):
            pos += 1
        elif(pos == 2):
            pos -= 1
    elif(s[i] == "B"):
        if(pos == 2):
            pos += 1
        elif(pos == 3):
            pos -= 1
    else:
        if(pos == 1):
            pos += 2
        elif(pos == 3):
            pos -= 2
print(pos)
