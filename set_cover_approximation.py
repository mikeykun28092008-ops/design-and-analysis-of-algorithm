def greedy_set_cover(universe, subsets):
    """Greedy approximation; subsets is a list of sets."""
    uncovered=set(universe); chosen=[]
    while uncovered:
        best=max(subsets,key=lambda s:len(set(s)&uncovered),default=set())
        gain=set(best)&uncovered
        if not gain: return None
        chosen.append(set(best)); uncovered-=gain
    return chosen

if __name__ == "__main__":
    print(greedy_set_cover({1,2,3,4},[{1,2},{2,3},{3,4}]))
