def container_loading(weights, capacity):
    """Greedy loading by lightest-first; returns chosen original indices."""
    chosen=[]; total=0
    for i,w in sorted(enumerate(weights),key=lambda x:x[1]):
        if total+w<=capacity: chosen.append(i); total+=w
    return chosen,total

if __name__ == "__main__":
    print(container_loading([10,40,20,30],50))
