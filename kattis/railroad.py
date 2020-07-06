xy = (input()).split(" ")
t = int(xy[0])*4+int(xy[1])*3
if(t % 2 == 0):
    print("possible")
else:
    print("impossible")
