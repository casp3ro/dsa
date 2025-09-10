def combination_sum(nums: list[int], target: int) -> list[list[int]]:
    """
    Finds all unique combinations that sum to target (numbers can be reused).
    
    Interview Tips:
    - Use DFS backtracking with index to avoid duplicates
    - At each step: include current number or skip to next
    - When including: stay at same index (reuse allowed)
    - When skipping: move to next index
    - Copy current combination when target is reached
    
    Complexity: O(2^(t/m)) time, O(t/m) space where t=target, m=min(nums)
    """
    output = []
    
    def dfs(index, current, value):
        if index >= len(nums) or value > target:
            return
        
        if value == target:
            output.append(current.copy())
            return
        
        current.append(nums[index])
        dfs(index, current, value + nums[index])
        
        current.pop()
        dfs(index + 1, current, value)
            
    dfs(0, [], 0)
    return output


def test_combination_sum():
    """Test function that can be run from terminal."""
    # Test: [2,3,6,7], target=7 -> [[2,2,3],[7]]
    nums = [2, 3, 6, 7]
    target = 7
    result = combination_sum(nums, target)
    print(f"Candidates: {nums}, Target: {target}")
    print(f"Combinations: {result}")


if __name__ == "__main__":
    test_combination_sum()