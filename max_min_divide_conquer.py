def max_min(a):
    if not a: raise ValueError("Input must not be empty")
    if len(a) == 1: return a[0], a[0]
    if len(a) == 2: return max(a), min(a)
    mid = len(a)//2
    max1, min1 = max_min(a[:mid])
    max2, min2 = max_min(a[mid:])
    return max(max1, max2), min(min1, min2)

if __name__ == "__main__":
    print("Maximum, minimum:", max_min([7, 2, 9, 4, 1, 6]))
