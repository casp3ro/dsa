def valid_tree(n: int, edges: list[list[int]]) -> bool:
    """
    Determines if edges form a valid tree (connected, no cycles, n-1 edges).
    
    Interview Tips:
    - Tree must have exactly n-1 edges
    - Must be connected (all nodes reachable)
    - Must have no cycles (use parent tracking in DFS)
    - Key insight: tree = connected + acyclic + n-1 edges
    
    Complexity: O(V + E) time, O(V) space where V=nodes, E=edges
    """
    if n == 1:
        return len(edges) == 0

    # Tree must have exactly n-1 edges
    if len(edges) != n - 1:
        return False

    def build_adjacency_list(edges_list: list) -> dict:
        adjacency_list = {}

        for v, e in edges_list:
            if v not in adjacency_list:
                adjacency_list[v] = []
            if e not in adjacency_list:
                adjacency_list[e] = []

            adjacency_list[v].append(e)
            adjacency_list[e].append(v)  # undirected

        return adjacency_list

    graph = build_adjacency_list(edges)
    visited = set()

    def dfs(node: int, parent: int) -> bool:
        if node in visited:
            return False  # cycle detected

        visited.add(node)

        for neighbour in graph[node]:
            if neighbour == parent:
                continue  # skip parent

            if not dfs(neighbour, node):
                return False

        return True

    return dfs(0, -1) and n == len(visited)


def test_valid_tree():
    """Test function that can be run from terminal."""
    # Test: n=5, edges=[[0,1],[0,2],[0,3],[1,4]] -> True (valid tree)
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    result = valid_tree(n, edges)
    print(f"Nodes: {n}, Edges: {edges}")
    print(f"Valid tree: {result}")


if __name__ == "__main__":
    test_valid_tree()
