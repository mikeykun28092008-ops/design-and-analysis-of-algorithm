def graph_coloring(graph, colors):
    """graph is an adjacency matrix; returns color numbers or None."""
    n=len(graph); assigned=[-1]*n
    def safe(v,c):
        return all(not graph[v][u] or assigned[u]!=c for u in range(n))
    def solve(v):
        if v==n: return True
        for c in range(colors):
            if safe(v,c):
                assigned[v]=c
                if solve(v+1): return True
                assigned[v]=-1
        return False
    return assigned if solve(0) else None

if __name__ == "__main__":
    g=[[0,1,1],[1,0,1],[1,1,0]]
    print(graph_coloring(g,3))
