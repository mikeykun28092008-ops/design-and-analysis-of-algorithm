def vertex_cover_2approx(vertices, edges):
    """2-approximation for an undirected graph; edges are (u,v)."""
    remaining=set(tuple(e) for e in edges); cover=set()
    while remaining:
        u,v=next(iter(remaining))
        cover.update((u,v))
        remaining={e for e in remaining if u not in e and v not in e}
    return cover

if __name__ == "__main__":
    print(vertex_cover_2approx(range(4),[(0,1),(1,2),(2,3)]))
