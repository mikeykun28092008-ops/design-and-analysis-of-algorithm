def bellman_ford(vertices, edges, source):
    """Edges are (u,v,weight); returns distances or raises on reachable negative cycle."""
    dist={v:float("inf") for v in vertices}; dist[source]=0
    for _ in range(len(vertices)-1):
        changed=False
        for u,v,w in edges:
            if dist[u]!=float("inf") and dist[u]+w<dist[v]:
                dist[v]=dist[u]+w; changed=True
        if not changed: break
    for u,v,w in edges:
        if dist[u]!=float("inf") and dist[u]+w<dist[v]:
            raise ValueError("Reachable negative-weight cycle")
    return dist

if __name__ == "__main__":
    print(bellman_ford([0,1,2,3],[(0,1,5),(1,2,3),(2,3,2),(0,3,10)],0))
