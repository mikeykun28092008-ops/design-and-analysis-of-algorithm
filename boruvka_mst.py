class DSU:
    def __init__(self,n): self.p=list(range(n))
    def find(self,x):
        if self.p[x]!=x: self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,a,b):
        a=self.find(a); b=self.find(b)
        if a==b: return False
        self.p[b]=a; return True

def boruvka(n, edges):
    """Vertices 0..n-1; edges are (weight,u,v)."""
    dsu=DSU(n); components=n; chosen=[]; total=0
    while components>1:
        cheapest={}
        for w,u,v in edges:
            a,b=dsu.find(u),dsu.find(v)
            if a!=b:
                if a not in cheapest or w<cheapest[a][0]: cheapest[a]=(w,u,v)
                if b not in cheapest or w<cheapest[b][0]: cheapest[b]=(w,u,v)
        if not cheapest: raise ValueError("Graph is disconnected")
        for w,u,v in cheapest.values():
            if dsu.union(u,v):
                chosen.append((u,v,w)); total+=w; components-=1
    return chosen,total

if __name__ == "__main__":
    print(boruvka(4,[(10,0,1),(6,0,2),(5,0,3),(15,1,3),(4,2,3)]))
