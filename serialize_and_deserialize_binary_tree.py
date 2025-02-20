class TreeNode:
    def __init__(self,val = 0, left =None, right = None):
        self.val = val
        self.left = left
        self.right = right
        


def serialize_and_deserialize_binary_tree():
    class Codec:
        def __init__(self):
            pass
        

        def serialize(self,root:TreeNode):
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
                
            
        def deserialize(self,data:str):
            data = data.split(',')
            self.i = 0
            
            def dfs(node):
                val = data[self.i]
                if val == 'N':
                    self.i +=1
                    return None
                
                self.i+=1
                node = TreeNode(val)
                
                node.left = dfs(node)
                node.right = dfs(node)
                
                return node
                
            node = dfs(TreeNode())
            
            return node
            
    