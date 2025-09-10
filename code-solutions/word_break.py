def word_break(s: str, wordDict: list[str]) -> bool:
    """
    Determines if a string can be segmented into dictionary words.
    
    Interview Tips:
    - Use dynamic programming: dp[i] = can segment s[i:]
    - Start from end and work backwards
    - For each position, try all dictionary words
    - dp[i] = True if word matches and dp[i+len(word)] = True
    
    Complexity: O(n*m*k) time, O(n) space where n=len(s), m=len(wordDict), k=avg word length
    """
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True
    
    for i in range(len(s) - 1, -1, -1):
        for word in wordDict:
            total_len = i + len(word)
            if total_len <= len(s) and s[i:total_len] == word:
                dp[i] = dp[total_len]
            if dp[i]:
                break
    
    return dp[0]


def test_word_break():
    """Test function that can be run from terminal."""
    # Test: "leetcode" with ["leet","code"] -> True
    s = "leetcode"
    wordDict = ["leet", "code"]
    result = word_break(s, wordDict)
    print(f"String: '{s}'")
    print(f"Dictionary: {wordDict}")
    print(f"Can be segmented: {result}")


if __name__ == "__main__":
    test_word_break()
                