def hamiltonian_cycle(graph):
    """graph is an adjacency matrix; returns a cycle or None."""
    n=len(graph)
    if n==0: return None
    path=[0]
    def backtrack():
        if len(path)==n: return graph[path[-1]][path[0]] != 0
        for v in range(1,n):
            if v not in path and graph[path[-1]][v]:
                path.append(v)
                if backtrack(): return True
                path.pop()
        return False
    return path+[path[0]] if backtrack() else None

if __name__ == "__main__":
    g=[[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]]
    print(hamiltonian_cycle(g))
