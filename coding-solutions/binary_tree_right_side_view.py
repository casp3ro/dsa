from collections import deque


class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Level order traversal to find the right side view
def binary_tree_right_side_view(root: TreeNode) -> list[int]:
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
