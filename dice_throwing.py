def count_dice_ways(dice, faces, target):
    """Number of ways to get target using dice fair dice with faces 1..faces."""
    dp=[0]*(target+1); dp[0]=1
    for _ in range(dice):
        nxt=[0]*(target+1)
        for total in range(target+1):
            for face in range(1,faces+1):
                if total+face<=target: nxt[total+face]+=dp[total]
        dp=nxt
    return dp[target]

if __name__ == "__main__":
    print(count_dice_ways(2, 6, 7))
