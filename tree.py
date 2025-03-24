from collections import deque


class TreeNode:
    def __init__(self, val:int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
        
def in_order(node:TreeNode):
    if not node:
        return
    
    in_order(node.left)
    print(node.val)
    in_order(node.right)
    

def pre_order(node:TreeNode):
    if not node:
        return
    
    print(node.val)
    pre_order(node.left)
    pre_order(node.right)
    
    
def post_order(node:TreeNode):
    if not node:
        return
    
    post_order(node.left)
    post_order(node.right)
    print(node.val)
    

def level_order(root:TreeNode):
    if not root:
        return
    
    queue = deque()
    queue.append(root)
    
    while queue:
        node = queue.popleft()
        print(node.val)
        
        if node.left:
            queue.append(node.left)
        
        if node.right:
            queue.append(node.right)
            

def level_order_grouped(root:TreeNode):
    if not root:
        return
    
    queue = deque()
    queue.append(root)
    
    while queue:
        queue_size = len(queue)
        level_nodes = []
        
        for _ in range(queue_size):
            node  = queue.popleft()
            
            level_nodes.append(node.val)
            
            if node.left:
                queue.append(node.left)
        
            if node.right:
                queue.append(node.right)
        
        print(level_nodes)
        