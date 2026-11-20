def first_fit_decreasing(items, capacity):
    """Approximation: sort items descending, then place in first fitting bin."""
    bins=[]
    for item in sorted(items,reverse=True):
        if item>capacity: raise ValueError("An item exceeds bin capacity")
        for b in bins:
            if sum(b)+item<=capacity: b.append(item); break
        else: bins.append([item])
    return bins

if __name__ == "__main__":
    print(first_fit_decreasing([4,8,1,4,2,1],10))
