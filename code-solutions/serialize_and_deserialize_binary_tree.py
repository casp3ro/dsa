class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    """
    Serializes and deserializes a binary tree using preorder traversal.
    
    Interview Tips:
    - Use preorder traversal (root, left, right)
    - Use 'N' to represent null nodes
    - Use comma as delimiter
    - Key insight: preorder allows reconstruction with single pass
    
    Complexity: O(n) time, O(n) space for both serialize and deserialize
    """
    def __init__(self):
        pass

    def serialize(self, root: TreeNode) -> str:
        res = []
        
        def dfs(node):
            if not node:
                res.append('N')
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ','.join(res)
            
    def deserialize(self, data: str) -> TreeNode:
        data = data.split(',')
        self.i = 0
        
        def dfs():
            val = data[self.i]
            if val == 'N':
                self.i += 1
                return None
            
            self.i += 1
            node = TreeNode(int(val))
            
            node.left = dfs()
            node.right = dfs()
            
            return node
            
        return dfs()


def test_serialize_and_deserialize_binary_tree():
    """Test function that can be run from terminal."""
    # Test: Tree [1,2,3,null,null,4,5] -> serialize -> deserialize
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    
    codec = Codec()
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    
    print(f"Original tree: [1,2,3,null,null,4,5]")
    print(f"Serialized: {serialized}")
    print(f"Deserialized successfully: {deserialized is not None}")


if __name__ == "__main__":
    test_serialize_and_deserialize_binary_tree()
            
    