def course_schedule(numCourses:int, prerequisites: list[list[int]])->bool:
    visited = set()
    graph = {i: [] for i in range(numCourses)}
    
    for u,v in prerequisites:
        graph[u].append(v)
        
    def dfs(node):
        if node in visited:
            return False
        
        if graph[node] == []:
            return True
        
        visited.add(node)
        
        for v in graph[node]:
            if not dfs(v):
                return False
        
        visited.remove(node)
        graph[node] = []
        
        return True
    
    
    for course in range(numCourses):
        if not dfs(course):
            return False
        
    return True