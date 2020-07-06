nbr = (input()).split(" ")

def rev(s):
    return s[::-1]

nbr1 = int(rev(nbr[0]))
nbr2 = int(rev(nbr[1]))

if(nbr1 > nbr2):
    print(nbr1)
else:
    print(nbr2)
