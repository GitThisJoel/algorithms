import sys
def djikstras(s,g,nodes):
    global graph
    global weights
    d=[0 for _ in range(len(nodes)+1)]
    d[0]=0
    for u in nodes:
        vs=graph[u]
        if len(vs)==1:
            v=graph[u][0]
            e=weights[(u,v)]
            if d[v]<d[u]+e:
                d[v]=d[u]+e
        else:
            v1,v2=vs
            e1=weights[(u,v1)]
            e2=weights[(u,v2)]
            if d[v1]<d[u]+e1:
                d[v1]=d[u]+e1
            if d[v2]<d[u]+e2:
                d[v2]=d[u]+e2
    return(d)
constw=int(input())
graph={}
weights={} # (u,v) -> w(v)
nodes={0}
prev=[0]
for line in sys.stdin:
    curr=[]
    for i in range(prev[-1]+1,prev[-1]+len(prev)+2):
        curr.append(i)
        nodes.add(i)
    ns=list(map(int,line.split()))
    for i in range(len(prev)):
        graph[prev[i]]=[curr[i],curr[i+1]]
        weights[(prev[i],curr[i])]=ns[i]
        weights[(prev[i],curr[i+1])]=ns[i+1]
    prev=curr
goal=prev[-1]+1
for u in prev:
    graph[u]=[goal]
    weights[(u,goal)]=constw
print(djikstras(0,goal,nodes)[-1])
