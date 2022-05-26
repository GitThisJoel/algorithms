# even: n -> n/2
# odd: n -> 3n+1

nbr = 0
chain = 0

for i in range(700000, 1000000): 
    nbrTmp = i
    chainTmp = 1

    while(nbrTmp != 1):
        if(nbrTmp % 2 == 0):
            nbrTmp = int(nbrTmp/2)
        else:
            nbrTmp = 3*nbrTmp+1
        chainTmp += 1
    if(chainTmp > chain):
        nbr = i
        chain = chainTmp

print(nbr)
print(chain)
