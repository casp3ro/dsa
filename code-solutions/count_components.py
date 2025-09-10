def count_components(n: int, edges: list[list[int]]) -> int:
    """
    Counts the number of connected components in an undirected graph.
    
    Interview Tips:
    - Use DFS to explore each connected component
    - Mark visited nodes to avoid revisiting
    - Each unvisited node starts a new component
    - Key insight: each DFS call explores one complete component
    
    Complexity: O(V + E) time, O(V) space where V=nodes, E=edges
    """
    response = 0
    visited = set()
    graph = {i: [] for i in range(n)}
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    def dfs(node):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                dfs(nei)
                
    for i in range(n):
        if i not in visited:
            dfs(i)
            response += 1
    
    return response


def test_count_components():
    """Test function that can be run from terminal."""
    # Test: 5 nodes, [[0,1],[1,2],[3,4]] -> 2 components
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    result = count_components(n, edges)
    print(f"Nodes: {n}, Edges: {edges}")
    print(f"Number of components: {result}")


if __name__ == "__main__":
    test_count_components()