def count_bits(n:int)-> list[int]:

    dp = [0] * (n+1)
    
    for num in range(n+1):
        dp[num] = dp[num>>1] + (num&1)
    
    return dp