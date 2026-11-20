def fractional_knapsack(weights, values, capacity):
    items=sorted(zip(weights,values),key=lambda x:x[1]/x[0],reverse=True)
    total=0.0
    for w,v in items:
        if capacity<=0: break
        take=min(w,capacity); total += take*(v/w); capacity-=take
    return total

if __name__ == "__main__":
    print(fractional_knapsack([10,20,30],[60,100,120],50))
