class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root:TreeNode)->int:
    if not root:
        return 0
    
    highest = float('-inf')
      
    def dfs(node:TreeNode):
        if not node:
            return 0
        
        leftVal = max(dfs(node.left), 0)
        rightVal = max(dfs(node.right), 0)
          
        highest = max((leftVal + rightVal + node.val), highest)    
        
        return node.val +max(leftVal,rightVal)
           
    dfs(root)
    
    return highest