def best_time_to_buy_sell_stock(prices:list[int]) -> int:
    left,right = 0,1
    max_profit = 0
    
    while right < len(prices):
        left_val = prices[left]
        right_val = prices[right]
        
        if left_val < right_val:
            curr_profit = right_val - left_val
            max_profit = max(max_profit,curr_profit)
        
        if left_val > right_val:
            left = right
        
        right +=1
        
    return max_profit
        