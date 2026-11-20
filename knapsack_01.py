def knapsack_01(weights, values, capacity):
    n=len(weights); dp=[0]*(capacity+1)
    for i in range(n):
        for cap in range(capacity,weights[i]-1,-1):
            dp[cap]=max(dp[cap],values[i]+dp[cap-weights[i]])
    return dp[capacity]

if __name__ == "__main__":
    print(knapsack_01([2,3,4,5],[3,4,5,6],5))
