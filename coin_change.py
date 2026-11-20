def coin_change_min(coins, amount):
    """Minimum number of coins; returns -1 if impossible."""
    dp=[float("inf")]*(amount+1); dp[0]=0
    for value in range(1,amount+1):
        for coin in coins:
            if coin<=value: dp[value]=min(dp[value],1+dp[value-coin])
    return dp[amount] if dp[amount]!=float("inf") else -1

if __name__ == "__main__":
    print(coin_change_min([1,2,5],11))
