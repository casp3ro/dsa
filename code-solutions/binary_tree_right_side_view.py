from collections import deque


class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_right_side_view(root: TreeNode) -> list[int]:
    """
    Returns the right side view of a binary tree (rightmost node at each level).
    
    Interview Tips:
    - Use BFS level-order traversal
    - Track queue size to process each level
    - Only add the last node (rightmost) at each level
    - Add children to queue for next level
    
    Complexity: O(n) time, O(w) space where w is max width of tree
    """
    right_side = []
    
    def bfs(root: TreeNode):
        if not root:
            return
        
        queue = deque()
        queue.append(root)
        
        while queue:
            queue_size = len(queue)

            for i in range(queue_size):
                node = queue.popleft()
                # Only the last element at each level
                if i == queue_size - 1:
                    right_side.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
    
    bfs(root)
    return right_side


def test_binary_tree_right_side_view():
    """Test function that can be run from terminal."""
    # Test: Tree [1,2,3,null,5,null,4] -> [1,3,4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    
    result = binary_tree_right_side_view(root)
    print(f"Right side view: {result}")


if __name__ == "__main__":
    test_binary_tree_right_side_view()
