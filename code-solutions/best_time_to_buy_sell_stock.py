def best_time_to_buy_sell_stock(prices: list[int]) -> int:
    """
    Finds the maximum profit from buying and selling stock once.
    
    Interview Tips:
    - Use two pointers: left (buy) and right (sell)
    - Only update buy pointer when we find a lower price
    - Always track maximum profit seen so far
    - Key insight: if price[right] < price[left], move left to right
    
    Complexity: O(n) time, O(1) space
    """
    left, right = 0, 1
    max_profit = 0
    
    while right < len(prices):
        left_val = prices[left]
        right_val = prices[right]
        
        if left_val < right_val:
            curr_profit = right_val - left_val
            max_profit = max(max_profit, curr_profit)
        
        if left_val > right_val:
            left = right
        
        right += 1
        
    return max_profit


def test_best_time_to_buy_sell_stock():
    """Test function that can be run from terminal."""
    # Test: [7,1,5,3,6,4] -> max profit = 5 (buy at 1, sell at 6)
    prices = [7, 1, 5, 3, 6, 4]
    result = best_time_to_buy_sell_stock(prices)
    print(f"Prices: {prices}")
    print(f"Max profit: {result}")


if __name__ == "__main__":
    test_best_time_to_buy_sell_stock()
        