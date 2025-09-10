
def min_cost_climbing_stairs(cost: list[int]) -> int:
    """
    Finds the minimum cost to climb stairs using dynamic programming.
    
    Interview Tips:
    - Use DP: cost[i] = min(cost[i+1], cost[i+2]) + cost[i]
    - Work backwards from the end
    - Add 0 at end to represent reaching the top
    - Key insight: at each step, choose minimum of next two steps
    
    Complexity: O(n) time, O(1) space
    """
    cost.append(0)
    
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])
        
    return min(cost[0], cost[1])


def test_min_cost_climbing_stairs():
    """Test function that can be run from terminal."""
    # Test: [10,15,20] -> 15 (climb step 1, then step 3)
    cost = [10, 15, 20]
    result = min_cost_climbing_stairs(cost)
    print(f"Costs: {cost}")
    print(f"Minimum cost: {result}")


if __name__ == "__main__":
    test_min_cost_climbing_stairs()