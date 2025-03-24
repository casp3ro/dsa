
# O(n * (2^n))
def subsets(nums: list[int]) -> list[int]:
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