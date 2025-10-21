import heapq


adjGraph = {
        'A': [(3, 'D', 'A'), (3, 'C', 'A'), (2, 'B', 'A')],
        'B': [(2, 'A', 'B'), (4, 'C', 'B'), (3, 'E', 'B')],
        'C': [(3, 'A', 'C'), (5, 'D', 'C'), (6, 'F', 'C'), (1, 'E', 'C'), (4, 'B', 'C')],
        'D': [(3, 'A', 'D'), (5, 'C', 'D'), (7, 'F', 'D')],
        'E': [(8, 'F', 'E'), (1, 'C', 'E'), (3, 'B', 'E')],
        'F': [(9, 'G', 'F'), (8, 'E', 'F'), (6, 'C', 'F'), (7, 'D', 'F')],
        'G': [(9, 'F', 'G')],
    }



def prims(graph:dict[str, list[tuple[int, str, str]]], start:str):
    visited = set() 
    total_cost = 0
    minimum_spanning_tree = []

    visited.add(start)

    heap = graph[start]
    heapq.heapify(heap)

    while heap and len(visited) < len(graph):
        cost, to_val, from_val = heapq.heappop(heap)
        node = None

        if  to_val not in visited and from_val in visited:
            node = to_val
            minimum_spanning_tree.append((from_val,to_val,cost))
        elif from_val not in visited and to_val in visited:
            node = from_val
            minimum_spanning_tree.append((to_val,from_val,cost))

        if node:
            visited.add(node)
            total_cost+=cost

            for n in graph[node]:
                heapq.heappush(heap,n)
    

    return minimum_spanning_tree,total_cost



print(prims(adjGraph,'A'))

    
