def count_components(n:int,edges:list[list[int]])->int:
    response = 0
    visited = set()
    graph = {i:[] for i in range(n)}
    
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    def dfs(node):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                dfs(nei)
                
    for i in range(n):
        if i not in visited:
            visited.add(i)
            dfs(i)
            response +=1
    
    return response