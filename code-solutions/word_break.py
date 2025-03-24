def word_break(s: str, wordDict: list[str]):
    dp = [False] * (len(s) +1)
    dp[len(s)] = True
    
    for i in range(len(s) -1,-1,-1):
        for word in wordDict:
            total_len = i + len(word)
            if total_len <= len(s) and s[i:total_len] == word:
                dp[i] = dp[total_len]
            if dp[i]:
                break
    
    return dp[0]
                