
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional['Node']) -> Optional['Node']:
    """
    Creates a deep copy of an undirected graph using DFS.
    
    Interview Tips:
    - Use hash map to map old nodes to new nodes
    - Use DFS to traverse and clone nodes
    - Check if node already cloned to avoid infinite loops
    - Clone neighbors recursively and add to new node's neighbors
    
    Complexity: O(V + E) time, O(V) space where V=vertices, E=edges
    """
    if not node:
        return None
    
    old_to_new = {}
    
    def dfs(node: Node):
        if node in old_to_new:
            return old_to_new[node]
    
        old_to_new[node] = Node(node.val)
        
        for neighbor in node.neighbors:
            new_neighbour = dfs(neighbor)
            old_to_new[node].neighbors.append(new_neighbour)
            
        return old_to_new[node]
        
    return dfs(node)


def test_clone_graph():
    """Test function that can be run from terminal."""
    # Test: Clone a simple graph
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.neighbors = [node2, node3]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node1, node2]
    
    cloned = clone_graph(node1)
    print(f"Original graph cloned successfully: {cloned is not None}")
    print(f"Cloned node value: {cloned.val if cloned else None}")


if __name__ == "__main__":
    test_clone_graph()
        
        