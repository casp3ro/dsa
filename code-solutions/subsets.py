
def subsets(nums: list[int]) -> list[list[int]]:
    """
    Generates all possible subsets of a given array.
    
    Interview Tips:
    - Use DFS backtracking to explore all combinations
    - At each index: include element or skip element
    - Copy current subset when adding to result
    - Backtrack by removing element after exploring
    
    Complexity: O(n * 2^n) time, O(n) space
    """
    output = []
    subsets = []

    def dfs(index):
        if index >= len(nums):
            output.append(subsets.copy())
            return

        subsets.append(nums[index])
        dfs(index + 1)

        subsets.pop()
        dfs(index + 1)

    dfs(0)
    return output


def test_subsets():
    """Test function that can be run from terminal."""
    # Test: [1,2,3] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    nums = [1, 2, 3]
    result = subsets(nums)
    print(f"Array: {nums}")
    print(f"Subsets: {result}")


if __name__ == "__main__":
    test_subsets()