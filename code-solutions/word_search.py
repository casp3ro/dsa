def word_search(board: list[list[str]], word: str) -> bool:
    """
    Searches for a word in a 2D board using DFS backtracking.
    
    Interview Tips:
    - Use DFS with backtracking to explore all paths
    - Mark cells as visited during exploration, unmark when backtracking
    - Check bounds, character match, and visited status
    - Try all 4 directions from each cell
    - Key insight: backtrack to explore all possible paths
    
    Complexity: O(m*n*4^L) time, O(L) space where L is word length
    """
    rows_length, cols_length = len(board), len(board[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
       
    def dfs(row, col, index):
        if index == len(word):
            return True
        
        if (row not in range(rows_length) or col not in range(cols_length) or 
            board[row][col] != word[index] or (row, col) in visited):
            return False
        
        visited.add((row, col))
        
        for dr, dc in directions:
            nr, nc = dr + row, dc + col
            if dfs(nr, nc, index + 1):
                return True
        
        visited.remove((row, col))
        return False
        
    for row in range(rows_length):
        for col in range(cols_length):
            if dfs(row, col, 0):
                return True
    
    return False


def test_word_search():
    """Test function that can be run from terminal."""
    # Test: Find "ABCCED" in board
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    result = word_search(board, word)
    print(f"Board: {board}")
    print(f"Word: '{word}'")
    print(f"Found: {result}")


if __name__ == "__main__":
    test_word_search()