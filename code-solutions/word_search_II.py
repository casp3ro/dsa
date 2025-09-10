
class TrieNode:
    def __init__(self, children=None, end=False):
        self.children = {} if children is None else children
        self.end = end


class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.end = True


def word_searchII(board: list[list[str]], words: list[str]) -> list[str]:
    """
    Finds all words from dictionary that exist in the board using Trie + DFS.
    
    Interview Tips:
    - Build Trie from all words for efficient prefix checking
    - Use DFS with backtracking to explore all paths
    - Check if current path forms a valid word prefix
    - Use visited set to avoid revisiting same cell
    - Key insight: Trie eliminates invalid paths early
    
    Complexity: O(m*n*4^L) time, O(W*L) space where W=words, L=max word length
    """
    visited, output = set(), set()
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    ROWS, COLS = len(board), len(board[0])
    trie = Trie()
    
    for word in words:
        trie.add(word)
    
    def dfs(r: int, c: int, node: TrieNode, word: str = ''):
        letter = board[r][c] 
        if letter not in node.children:
            return

        word += letter
        node = node.children[letter]
        
        if node.end:
            output.add(word)
            
        visited.add((r, c))
        
        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            
            if (nr in range(ROWS) and nc in range(COLS) and 
                (nr, nc) not in visited and board[nr][nc] in node.children):
                dfs(nr, nc, node, word)
        
        visited.remove((r, c))

    for r in range(ROWS):
        for c in range(COLS):
            dfs(r, c, trie.root)

    return list(output)


def test_word_searchII():
    """Test function that can be run from terminal."""
    # Test: Board with words "oath","pea","eat","rain"
    board = [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
    words = ["oath","pea","eat","rain"]
    result = word_searchII(board, words)
    print(f"Board: {board}")
    print(f"Words: {words}")
    print(f"Found: {result}")


if __name__ == "__main__":
    test_word_searchII()