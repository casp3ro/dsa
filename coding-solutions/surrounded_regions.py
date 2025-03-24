def surrounded_regions(board: list[int]):
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
    
    for row in range(rows_length):
        for col in range(cols_length):
            if board[row][col] == 'O':
                board[row][col] = 'X'
            if board[row][col] == 'T':
                board[row][col] = 'O'
