class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: TreeNode) -> int:
    """
    Finds the maximum path sum in a binary tree using DFS.
    
    Interview Tips:
    - Use DFS to explore all paths
    - For each node, consider path through it (left + right + node)
    - Return max path ending at current node (node + max(left, right))
    - Use nonlocal to update global maximum
    - Key insight: path can go through any node as the "peak"
    
    Complexity: O(n) time, O(h) space where h is height
    """
    if not root:
        return 0
    
    highest = float('-inf')
      
    def dfs(node: TreeNode):
        nonlocal highest
        if not node:
            return 0
        
        leftVal = max(dfs(node.left), 0)
        rightVal = max(dfs(node.right), 0)
          
        highest = max((leftVal + rightVal + node.val), highest)    
        
        return node.val + max(leftVal, rightVal)
           
    dfs(root)
    return highest


def test_max_path_sum():
    """Test function that can be run from terminal."""
    # Test: Tree [1,2,3] -> max path = 6 (2->1->3)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    result = max_path_sum(root)
    print(f"Tree: [1,2,3]")
    print(f"Maximum path sum: {result}")


if __name__ == "__main__":
    test_max_path_sum()