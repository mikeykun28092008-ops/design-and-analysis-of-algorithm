def binomial(n, k):
    if n < 0 or k < 0 or k > n: return 0
    dp=[0]*(k+1); dp[0]=1
    for i in range(1,n+1):
        for j in range(min(i,k),0,-1):
            dp[j] += dp[j-1]
    return dp[k]

if __name__ == "__main__":
    print(binomial(5,2))
