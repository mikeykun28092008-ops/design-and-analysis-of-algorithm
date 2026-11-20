def subset_sum(numbers, target):
    result=[]
    def search(i,total,chosen):
        if total==target: result.append(chosen[:]); return
        if i==len(numbers) or total>target: return
        search(i+1,total+numbers[i],chosen+[numbers[i]])
        search(i+1,total,chosen)
    search(0,0,[])
    return result

if __name__ == "__main__":
    print(subset_sum([3,4,5,2],9))
