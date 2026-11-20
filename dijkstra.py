import heapq

def dijkstra(graph, source):
    """graph[u] = iterable of (neighbor, nonnegative_weight)."""
    dist={v:float("inf") for v in graph}; dist[source]=0
    pq=[(0,source)]
    while pq:
        d,u=heapq.heappop(pq)
        if d!=dist[u]: continue
        for v,w in graph[u]:
            if w<0: raise ValueError("Dijkstra requires nonnegative edge weights")
            if d+w<dist.get(v,float("inf")):
                dist[v]=d+w; heapq.heappush(pq,(d+w,v))
    return dist

if __name__ == "__main__":
    g={"A":[("B",4),("C",1)],"B":[("D",1)],"C":[("B",2),("D",5)],"D":[]}
    print(dijkstra(g,"A"))
