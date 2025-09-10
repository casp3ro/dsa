def surrounded_regions(board: list[list[str]]) -> None:
    """
    Captures surrounded regions by marking border-connected 'O's and flipping others to 'X'.
    
    Interview Tips:
    - Start DFS from border 'O's (not surrounded)
    - Mark border-connected 'O's as 'T' (temporary)
    - Flip remaining 'O's to 'X' (surrounded)
    - Flip 'T's back to 'O' (not surrounded)
    - Key insight: work backwards from border, not from interior
    
    Complexity: O(m*n) time, O(m*n) space
    """
    rows_length, cols_length = len(board), len(board[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def dfs(row, col):     
        board[row][col] = 'T'
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (
                new_row in range(rows_length) and
                new_col in range(cols_length) and
                board[new_row][new_col] == 'O'
            ):
                dfs(new_row, new_col)
    
    # Mark border-connected 'O's
    for row in range(rows_length):
        if board[row][0] == 'O':
            dfs(row, 0)
        if board[row][cols_length - 1] == 'O':
            dfs(row, cols_length - 1)
    
    for col in range(cols_length):
        if board[0][col] == 'O':
            dfs(0, col)
        if board[rows_length - 1][col] == 'O':
            dfs(rows_length - 1, col)
    
    # Flip remaining 'O's to 'X' and 'T's back to 'O'
    for row in range(rows_length):
        for col in range(cols_length):
            if board[row][col] == 'O':
                board[row][col] = 'X'
            if board[row][col] == 'T':
                board[row][col] = 'O'


def test_surrounded_regions():
    """Test function that can be run from terminal."""
    # Test: Board with surrounded regions
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    print(f"Original board: {board}")
    surrounded_regions(board)
    print(f"After capture: {board}")


if __name__ == "__main__":
    test_surrounded_regions()
