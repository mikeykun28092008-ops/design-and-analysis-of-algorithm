from bisect import bisect_right

def weighted_interval_scheduling(jobs):
    """Each job is (start, finish, profit). Returns maximum profit."""
    jobs=sorted(jobs,key=lambda x:x[1])
    ends=[job[1] for job in jobs]
    dp=[0]*(len(jobs)+1)
    for i,(start,finish,profit) in enumerate(jobs,1):
        p=bisect_right(ends,start,0,i-1)
        dp[i]=max(dp[i-1],profit+dp[p])
    return dp[-1]

if __name__ == "__main__":
    print(weighted_interval_scheduling([(1,3,5),(2,5,6),(4,6,5),(6,7,4),(5,8,11),(7,9,2)]))
