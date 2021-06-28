import sys
contains=0
counter=1
def area(x1,y1, x2,y2, x3,y3):
    return abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2.0)
for line in sys.stdin:
    trig=list(map(int, line.split(',')))
    x,y=0,0
    x1,y1=trig[0],trig[1]
    x2,y2=trig[2],trig[3]
    x3,y3=trig[4],trig[5]

    # d1=(y2-y1)*(x-x1)+(-x2+x1)*(y-y1)
    # d2=(y3-y2)*(x-x2)+(-x3+x2)*(y-y2)
    # d3=(y1-y3)*(x-x3)+(-x1+x3)*(y-y3)
    # if d1>=0 and d2>=0 and d3>=0:
    #     contains+=1
    AT =area(x1,y1,x2,y2,x3,y3)
    AT1=area(x,y,x2,y2,x3,y3)
    AT2=area(x1,y1,x,y,x3,y3)
    AT3=area(x1,y1,x2,y2,x,y)
    if AT==(AT1+AT2+AT3):
        contains+=1
    print(x1,y1,x2,y2,x3,y3)
    print(AT,AT1,AT2,AT3)
    print(AT1+AT2+AT3)

print(contains)
