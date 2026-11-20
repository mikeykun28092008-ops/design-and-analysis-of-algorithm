def select_kth(a, k):
    """1-based k-th smallest, using median-of-medians selection."""
    if not 1 <= k <= len(a): raise ValueError("k out of range")
    if len(a) <= 5: return sorted(a)[k-1]
    groups=[sorted(a[i:i+5]) for i in range(0,len(a),5)]
    medians=[g[len(g)//2] for g in groups]
    pivot=select_kth(medians,(len(medians)+1)//2)
    low=[x for x in a if x<pivot]
    equal=[x for x in a if x==pivot]
    high=[x for x in a if x>pivot]
    if k<=len(low): return select_kth(low,k)
    if k<=len(low)+len(equal): return pivot
    return select_kth(high,k-len(low)-len(equal))

if __name__ == "__main__":
    print(select_kth([7,10,4,3,20,15], 3))
