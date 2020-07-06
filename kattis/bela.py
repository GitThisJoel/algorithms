# VALUES
#       A  K Q J  T  9  8 7
# D     11 4 3 20 10 14 0 0
# notD  11 4 3 2  10 0  0 0

card = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7']
D    = [11, 4, 3, 20, 10, 14, 0, 0]
notD = [11, 4, 3, 2,  10,  0, 0, 0]

import sys
xs = []
for line in sys.stdin:
    xs.append(line)
dominant = xs[0].split(" ")[1][0]

tot = 0
for i in range(1, len(xs), 4):
    for j in range(0, 4):
        if(xs[i+j][1] == dominant):
            tot += D[card.index(xs[i+j][0])]
        else:
            tot += notD[card.index(xs[i+j][0])]
print(tot)
