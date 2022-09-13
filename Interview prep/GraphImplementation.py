from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.V=vertices
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def printGraph(self):
        temp=self.graph
        for x in temp:
            print(x,"-->",temp[x])
    def iscyclic(self):
        stack=[0]
        visited=[]
        temp=self.graph
        
        while stack:
            current=stack.pop()
            for neighbour in temp[current]:
                if neighbour not in visited:
                    stack.append(neighbour)
                else:
                    return 'True'
            visited.append(current)
        return 'False'                
                
if __name__=='__main__':
    N=int(input())
    g=Graph(N)
    edges=list(map(int,input().strip().split()))
    for i in range(0,len(edges),2):
        u,v=edges[i],edges[i+1]
        g.addEdge(u,v)
        '''g.addEdge(v,u)'''
    g.printGraph()
    print(g.iscyclic())
