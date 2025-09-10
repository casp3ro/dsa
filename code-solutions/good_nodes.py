from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def good_nodes_dfs(root: TreeNode) -> int:
    """
    Counts good nodes in binary tree using DFS (node is good if >= max value from root).
    
    Interview Tips:
    - Use DFS with current maximum value
    - Pass current max down the recursion
    - Update max when visiting each node
    - Key insight: track maximum value seen so far in path
    
    Complexity: O(n) time, O(h) space where h is height
    """
    count = 0
    
    def dfs(node: TreeNode, currMax: int):  
        nonlocal count
        if not node:
            return
        
        if node.val >= currMax:
            count += 1
    
        currMax = max(node.val, currMax)
        
        if node.left:
            dfs(node.left, currMax)
        
        if node.right:
            dfs(node.right, currMax)
    
    dfs(root, root.val)
    return count


def good_nodes_bfs(root: TreeNode) -> int:
    """
    Counts good nodes in binary tree using BFS.
    
    Interview Tips:
    - Use BFS with queue storing (node, currentMax)
    - Update currentMax for each child
    - Key insight: BFS processes level by level with max tracking
    
    Complexity: O(n) time, O(w) space where w is max width
    """
    count = 0
    
    def bfs(treeNode: TreeNode):
        nonlocal count
        if not treeNode:
            return
        
        queue = deque()
        queue.append((treeNode, treeNode.val))
        
        while queue:
            node, currMax = queue.popleft()
            
            if node.val >= currMax:
                count += 1
                
            if node.left:
                queue.append((node.left, max(node.val, currMax)))
            if node.right:
                queue.append((node.right, max(node.val, currMax)))
        
    bfs(root)
    return count


def test_good_nodes():
    """Test function that can be run from terminal."""
    # Test: Tree [3,1,4,3,null,1,5] -> 4 good nodes
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)
    
    result_dfs = good_nodes_dfs(root)
    result_bfs = good_nodes_bfs(root)
    print(f"Tree: [3,1,4,3,null,1,5]")
    print(f"Good nodes (DFS): {result_dfs}")
    print(f"Good nodes (BFS): {result_bfs}")


if __name__ == "__main__":
    test_good_nodes()