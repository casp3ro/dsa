def coin_change(coins:list[int], amount:int):
    if not coins:
        return -1
    if amount == 0:
        return 0
    
    
    dp = [float('inf')] * (amount +1)
    
    dp[0] = 0
    
    for a in range(1,amount+1):
        for c in coins:
            if a -c >=0:
                dp[a] = min(dp[a], dp[a-c] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1