def valid_tree(n: int, edges: list[list[int]]) -> bool:
    if n == 1:
        return len(edges) == 0

    def build_adjacency_list(edges_list: list) -> dict:
        adjacency_list = {}

        for v, e in edges_list:
            if v not in adjacency_list:
                adjacency_list[v] = []
            if e not in adjacency_list:
                adjacency_list[e] = []

            adjacency_list[v].append(e)
            adjacency_list[e].append(v)  # only for undirected

        return adjacency_list

    graph = build_adjacency_list(edges)
    visited = set()

    def dfs(node: int, parent: int) -> bool:
        if node in visited:
            return False

        visited.add(node)

        for neighbour in graph[node]:
            if neighbour == parent:
                continue

            if not dfs(neighbour, node):
                return False

        return True

    return dfs(0, -1) and n == len(visited)
