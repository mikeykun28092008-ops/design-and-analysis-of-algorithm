import heapq

def prim_mst(graph, start):
    """Undirected weighted graph: graph[u] = [(v, weight), ...]."""
    visited={start}; edges=[]; total=0; pq=[]
    for v,w in graph[start]: heapq.heappush(pq,(w,start,v))
    while pq:
        w,u,v=heapq.heappop(pq)
        if v in visited: continue
        visited.add(v); edges.append((u,v,w)); total+=w
        for nxt,cost in graph[v]:
            if nxt not in visited: heapq.heappush(pq,(cost,v,nxt))
    if len(visited)!=len(graph): raise ValueError("Graph is disconnected")
    return edges,total

if __name__ == "__main__":
    g={"A":[("B",1),("C",3)],"B":[("A",1),("C",2)],"C":[("A",3),("B",2)]}
    print(prim_mst(g,"A"))
