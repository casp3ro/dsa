def max_area_of_island(grid: list[list[int]]) -> int:
    """
    Finds the maximum area of an island in a 2D grid using DFS.
    
    Interview Tips:
    - Use DFS to explore each connected component (island)
    - Mark visited cells to avoid revisiting
    - Count cells in each island and track maximum
    - Check all 4 directions from each cell
    - Key insight: each DFS call explores one complete island
    
    Complexity: O(m*n) time, O(m*n) space
    """
    rows_len, cols_len = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_area = 0
    visited = set()

    def dfs(start_row, start_col):
        visited.add((start_row, start_col))
        counter = 1

        for dr, dc in directions:
            nr, nc = start_row + dr, start_col + dc

            if (
                nr in range(rows_len)
                and nc in range(cols_len)
                and grid[nr][nc] == 1
                and (nr, nc) not in visited
            ):
                counter += dfs(nr, nc)

        return counter

    for row in range(rows_len):
        for col in range(cols_len):
            if grid[row][col] == 1 and (row, col) not in visited:
                counter = dfs(row, col)
                max_area = max(max_area, counter)

    return max_area


def test_max_area_of_island():
    """Test function that can be run from terminal."""
    # Test: Grid with islands, max area = 6
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    result = max_area_of_island(grid)
    print(f"Grid has multiple islands")
    print(f"Maximum island area: {result}")


if __name__ == "__main__":
    test_max_area_of_island()
