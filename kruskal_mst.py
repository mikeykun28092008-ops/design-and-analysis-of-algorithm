class DSU:
    def __init__(self,n): self.p=list(range(n)); self.r=[0]*n
    def find(self,x):
        if self.p[x]!=x: self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,a,b):
        a=self.find(a); b=self.find(b)
        if a==b: return False
        if self.r[a]<self.r[b]: a,b=b,a
        self.p[b]=a
        if self.r[a]==self.r[b]: self.r[a]+=1
        return True

def kruskal(n, edges):
    """Vertices are 0..n-1; edges are (weight,u,v)."""
    dsu=DSU(n); chosen=[]; total=0
    for w,u,v in sorted(edges):
        if dsu.union(u,v): chosen.append((u,v,w)); total+=w
    if len(chosen)!=n-1 and n>0: raise ValueError("Graph is disconnected")
    return chosen,total

if __name__ == "__main__":
    print(kruskal(4,[(10,0,1),(6,0,2),(5,0,3),(15,1,3),(4,2,3)]))
