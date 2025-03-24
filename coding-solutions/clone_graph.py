
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node: Optional['Node']) -> Optional['Node']:
    
    if not node:
        return None
    
    old_to_new = {}
    
    def dfs(node:Node):
        if node in old_to_new:
            return old_to_new[node]
    
        old_to_new[node] = Node(node.val)
        
        for neighbor in node.neighbors:
            new_neighbour = dfs(neighbor)
            old_to_new[node].neighbors.append(new_neighbour)
            
        return old_to_new[node]
        
        
    return dfs(node)
        
        