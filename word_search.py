def word_search(board:list[list[str]],word:str)-> bool:
    
    rows_length, cols_length = len(board), len(board[0])
    
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    visited = set()
       
    def dfs (row, col,index):
        if index == len(word):
            return True
        
        if row not in range(rows_length) or col not in range(cols_length) or board[row][col] != word[index] or (row,col) in visited:
            return False
        
        visited.add((row,col))
        
        for dr,dc in directions:
            nr,nc = dr + row, dc +col
            if dfs(nr,nc,index+1):
                return True
        
        visited.remove((row,col))
        
        return False
        
    
    for row in range(rows_length):
        for col in range(cols_length):
            if dfs(row,col,0):
                return True
    
    return False