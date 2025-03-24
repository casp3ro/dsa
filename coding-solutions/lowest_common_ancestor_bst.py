class TreeNode:
    def __init__(self, val=int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def lowest_common_ancestor_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    node = root
    
    while node:
        if p.val > node.val and q.val > node.val:
            node = node.right
        elif p.val < node.val and q.val < node.val:
            node = node.left
        else:
            return node