from functools import lru_cache

def tsp(cost):
    """Held-Karp DP; cost[i][j] is travel cost from i to j."""
    n=len(cost)
    if n==0: return 0, []
    @lru_cache(None)
    def dp(mask,last):
        if mask==(1<<n)-1: return cost[last][0], (last,0)
        best=float("inf"); best_path=()
        for nxt in range(n):
            if not mask>>nxt&1:
                value,path=dp(mask|1<<nxt,nxt)
                value += cost[last][nxt]
                if value<best: best,best_path=value,(last,)+path
        return best,best_path
    value,path=dp(1,0)
    return value,list(path)

if __name__ == "__main__":
    c=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
    print(tsp(c))
