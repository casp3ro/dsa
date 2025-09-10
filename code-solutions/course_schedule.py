def course_schedule(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """
    Determines if all courses can be completed (detects cycles in directed graph).
    
    Interview Tips:
    - Use DFS to detect cycles in directed graph
    - Track visited nodes during current path
    - If node is visited again in same path = cycle
    - Mark node as processed after exploring all neighbors
    - Key insight: cycle detection with three states (unvisited, visiting, visited)
    
    Complexity: O(V + E) time, O(V) space where V=courses, E=prerequisites
    """
    visited = set()
    graph = {i: [] for i in range(numCourses)}
    
    for u, v in prerequisites:
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


def test_course_schedule():
    """Test function that can be run from terminal."""
    # Test: 2 courses, [[1,0]] -> True (can take course 0 then course 1)
    numCourses = 2
    prerequisites = [[1, 0]]
    result = course_schedule(numCourses, prerequisites)
    print(f"Courses: {numCourses}")
    print(f"Prerequisites: {prerequisites}")
    print(f"Can complete all courses: {result}")


if __name__ == "__main__":
    test_course_schedule()