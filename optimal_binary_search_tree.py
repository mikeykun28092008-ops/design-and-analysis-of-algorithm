def optimal_bst(freq):
    """Minimum search cost for successful-search frequencies only."""
    n=len(freq); dp=[[0]*n for _ in range(n)]
    prefix=[0]
    for f in freq: prefix.append(prefix[-1]+f)
    for length in range(1,n+1):
        for i in range(n-length+1):
            j=i+length-1; total=prefix[j+1]-prefix[i]
            dp[i][j]=min((dp[i][r-1] if r>i else 0)+(dp[r+1][j] if r<j else 0)+total for r in range(i,j+1))
    return dp[0][n-1] if n else 0

if __name__ == "__main__":
    print(optimal_bst([34,8,50]))
