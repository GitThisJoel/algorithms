#a**b, a,b<100
#vad är max siffer summa?

maxSum = 0
at = (0, 0)

def nbrSum(nbr):
    sum = 0
    for i in range(0, len(str(nbr))):
        sum += int(str(nbr)[i])
        i += 1
    return sum


for a in range(2, 101):
    for b in range(2, 101):
        tempSum = nbrSum(a**b)
        if(tempSum > maxSum):
            maxSum = tempSum
            at = (a, b)
        b += 1
    a += 1

print(maxSum)
print(at)
