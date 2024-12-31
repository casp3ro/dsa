from collections import deque

class TreeNode:
    def __init__(self,val,left= None,right = None):
        self.val = val
        self.left = left
        self.right  = right
        


def good_nodes_dfs(self,root:TreeNode):
    
    self.count = 0
    
    def dfs(node:TreeNode,currMax:int):  
        if not node:
            return
        
        if node.val >=currMax:
            self.count +=1
    
        currMax = max(node.val,currMax)
        
        if node.left:
            dfs(node.left,currMax)
        
        if node.right:
            dfs(node.right,currMax)
    
    
    dfs(root,root.val)
    
    return self.count


def good_nodes_bfs(self,root: TreeNode):
    self.count = 0
    
    def bfs(treeNode:TreeNode):
        if not treeNode:
            return
        
        queue = deque()
        queue.append((treeNode,treeNode.val))
        
        while queue:
            node, currMax = queue.popleft()
            
            if node.val >=currMax:
                self.count +=1
                
            if node.left:
                queue.append((node.left, max(node.val, currMax)))
            if node.right:
                queue.append((node.right,max(node.val, currMax)))
        
    bfs(root)
    
    return self.count