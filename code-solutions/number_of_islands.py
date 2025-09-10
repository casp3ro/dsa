from collections import deque


def number_of_islands(grid: list[list[str]]) -> int:
    """
    Counts the number of islands in a 2D grid using BFS.
    
    Interview Tips:
    - Use BFS to explore connected '1's (islands)
    - Mark visited cells to avoid revisiting
    - Check all 4 directions from each cell
    - Increment count for each unvisited '1' found
    - Key insight: each BFS call explores one complete island
    
    Complexity: O(m*n) time, O(m*n) space
    """
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
                if (neighbor_row in range(rows_length) and neighbor_col in range(cols_length) and 
                    (neighbor_row, neighbor_col) not in visited and grid[neighbor_row][neighbor_col] == '1'):
                    queue.append((neighbor_row, neighbor_col))
                    visited.add((neighbor_row, neighbor_col))
    
    for r in range(rows_length):
        for c in range(cols_length):
            if (r, c) not in visited and grid[r][c] == '1':
                bfs(r, c)
                islands += 1
                
    return islands


def test_number_of_islands():
    """Test function that can be run from terminal."""
    # Test: 3 islands in grid
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    result = number_of_islands(grid)
    print(f"Grid: {grid}")
    print(f"Number of islands: {result}")


if __name__ == "__main__":
    test_number_of_islands()
