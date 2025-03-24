
class TrieNode:
    def __init__(self, children =None, end =False):
        self.children = {} if children is  None else children
        self.end = end 
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr  = curr.children[char]
        
        curr.end = True
            
    


def word_searchII( board: list[list[str]], words: list[str]) -> list[str]:
    visited, output  = set(), set()
    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    ROWS, COLS = len(board), len(board[0])
    trie = Trie()
    
    for word in words:
        trie.add(word)
    
    
    def dfs(r:str,c:str,node:TrieNode,word = ''):
        letter = board[r][c] 
        if letter not in node.children:
            return

        word += letter
        node = node.children[letter]
        
        if node.end:
            output.add(word)
            
        visited.add((r,c))
        
        for dr,dc in directions:
            nr,nc = dr+r, dc+c
            
            if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visited and board[nr][nc] in node.children:
                dfs(nr,nc,node,word)
        
        visited.remove((r,c))
            

    for r in range(ROWS):
        for c in range(COLS):
            dfs(r,c,trie.root)

    
    return list(output)