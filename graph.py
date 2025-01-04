from collections import deque


class Graph:
    def __init__(self):
        pass
 
    def build_adjacency_list(self,edges: list[list[str]],undirected:bool = False):
        adjacency_list = {}
        
        for item in edges:
            node = item[0]
            neighbours = item[1:]
            
            if node not in adjacency_list:
                adjacency_list[node] = []
                
            for neighbour in neighbours:
                adjacency_list[node].append(neighbour)
                
                if undirected:
                    if neighbour not in adjacency_list:
                        adjacency_list[neighbour] = []
                    adjacency_list[neighbour].append(node)
                
        return adjacency_list
    
    
    def dfs_adjacency(self,graph,node,visited = None):
        if not visited:
            visited = set()

        if node in visited:
            return
        
        visited.add(node)
        
        print(node)
        
        for neighbour in graph[node]:
            self.dfs_adjacency(neighbour,graph,visited)
            
    def bfs_adjacency(self,graph,initial_node):
        visited = set()
        queue = deque()
        
        visited.add(initial_node)
        queue.append(initial_node)
        
        while queue:
            node = queue.popleft()
            print(node)
            for neighbour in graph[node]:
                if neighbour not in visited: 
                    visited.add(neighbour)
                    queue.append(neighbour)
            
            
    

list = [['A', 'B', 'G'],
 ['B', 'C', 'D', 'E'],
 ['C'],
 ['D'],
 ['E', 'F'],
 ['F'],
 ['G', 'H'],
 ['H', 'I'],
 ['I']]

expected_directed_adj_list = {
  'A' : ['B','G'],
  'B' : ['C', 'D', 'E'],
  'C' : [],
  'D' : [],
  'E' : ['F'],
  'F' : [],
  'G' : ['H'],
  'H' : ['I'],
  'I' : [],
}


graph = Graph() 

adj_list = graph.build_adjacency_list(list)  

print('Are adj list the same:', expected_directed_adj_list == adj_list)

print('BFS')
graph.bfs_adjacency(adj_list, 'A')

print('DFS')
graph.bfs_adjacency(adj_list, 'A')