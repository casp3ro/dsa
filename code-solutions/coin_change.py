def coin_change(coins: list[int], amount: int) -> int:
    """
    Finds the minimum number of coins needed to make up the given amount.
    
    Interview Tips:
    - Use dynamic programming: dp[i] = min coins for amount i
    - Initialize dp[0] = 0, others as infinity
    - For each amount, try each coin: dp[i] = min(dp[i], dp[i-coin] + 1)
    - Return -1 if amount is impossible to make
    
    Complexity: O(amount * coins) time, O(amount) space
    """
    if not coins:
        return -1
    if amount == 0:
        return 0
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], dp[a - c] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def test_coin_change():
    """Test function that can be run from terminal."""
    # Test: coins=[1,3,4], amount=6 -> 2 coins (3+3)
    coins = [1, 3, 4]
    amount = 6
    result = coin_change(coins, amount)
    print(f"Coins: {coins}, Amount: {amount}")
    print(f"Minimum coins needed: {result}")


if __name__ == "__main__":
    test_coin_change()