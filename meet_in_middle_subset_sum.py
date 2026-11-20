def subset_sum_mitm(numbers, target):
    def sums(arr):
        result=[0]
        for x in arr: result += [s+x for s in result]
        return result
    mid=len(numbers)//2
    left=sums(numbers[:mid]); right=set(sums(numbers[mid:]))
    return any(target-x in right for x in left)

if __name__ == "__main__":
    print(subset_sum_mitm([3, 34, 4, 12, 5, 2], 9))
