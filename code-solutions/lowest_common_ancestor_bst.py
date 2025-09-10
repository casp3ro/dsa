class TreeNode:
    def __init__(self, val=int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Finds the lowest common ancestor of two nodes in a BST.
    
    Interview Tips:
    - Use BST property: left < root < right
    - If both nodes > current, go right
    - If both nodes < current, go left
    - Otherwise, current is LCA
    - Key insight: LCA is where paths diverge
    
    Complexity: O(h) time, O(1) space where h is height
    """
    node = root
    
    while node:
        if p.val > node.val and q.val > node.val:
            node = node.right
        elif p.val < node.val and q.val < node.val:
            node = node.left
        else:
            return node


def test_lowest_common_ancestor_bst():
    """Test function that can be run from terminal."""
    # Test: BST with nodes 2 and 8, LCA should be 6
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    
    p = root.left  # node 2
    q = root.right  # node 8
    result = lowest_common_ancestor_bst(root, p, q)
    print(f"BST: [6,2,8,0,4,7,9]")
    print(f"LCA of nodes 2 and 8: {result.val}")


if __name__ == "__main__":
    test_lowest_common_ancestor_bst()