from collections import deque
from typing import List

# O(m * n)

def number_of_islands(grid: List[List[str]]) -> int:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    queue = deque()
    islands = 0
    
    rows_length, cols_length = len(grid), len(grid[0])
    
    def bfs(start_row, start_col):
        queue.append((start_row, start_col))
        visited.add((start_row, start_col))
        
        while queue:
            current_row, current_col = queue.popleft()
            
            for dr, dc in directions:
                neighbor_row, neighbor_col = current_row + dr, current_col + dc
                if neighbor_row in range(rows_length) and neighbor_col in range(cols_length) and (neighbor_row, neighbor_col) not in visited and grid[neighbor_row][neighbor_col] == '1':
                    queue.append((neighbor_row, neighbor_col))
                    visited.add((neighbor_row, neighbor_col))
    
    for r in range(rows_length):
        for c in range(cols_length):
            if (r, c) not in visited and grid[r][c] == '1':
                bfs(r, c)
                islands += 1
                
    return islands
