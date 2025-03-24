
# O(n) time
# 1 DP
def min_cost_climbing_stairs(cost:list[int]):
    
    cost.append(0)
    
    for i in range(len(cost) -3,-1,-1):
        cost[i] += min(cost[i +1], cost[i+2])
        
    return min(cost[i], cost[i+1])