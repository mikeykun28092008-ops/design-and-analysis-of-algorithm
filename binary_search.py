def binary_search(a, target):
    """Return index of target in sorted list, or -1."""
    lo, hi = 0, len(a)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if a[mid] == target: return mid
        if a[mid] < target: lo = mid+1
        else: hi = mid-1
    return -1

if __name__ == "__main__":
    data = [1, 3, 5, 7, 9]
    print(binary_search(data, 7))
