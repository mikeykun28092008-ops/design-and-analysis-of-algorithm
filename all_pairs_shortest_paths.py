def floyd_warshall(graph):
    """graph is a square matrix; use float('inf') for no edge."""
    n=len(graph); dist=[row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k]+dist[k][j]<dist[i][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
    return dist

if __name__ == "__main__":
    inf=float("inf")
    print(floyd_warshall([[0,3,inf],[inf,0,1],[2,inf,0]]))
