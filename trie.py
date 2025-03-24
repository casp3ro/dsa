class TrieNode:
    def __init__(self, val:str = ''):
        self.val = val
        self.children = {}
        self.end = False     

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self,word:str):
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        
        curr.end = True
    
    def search(self,word:str):
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
        
        return curr.end 
    
    
    def starts_with(self,prefix: str):
        curr = self.root
        
        for char in prefix:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
        
        return True
    
    def list_words(self):
        words = []
        
        def dfs(node:TrieNode,word = ''):
            if not node:
                return
            
            currWord = word+node.val
            
            if node.end:
                words.append(currWord)
                
            for child in node.children.values():
                dfs(child,currWord)
        
        dfs(self.root)
        
        return words
    
    def count_words(self):
        list_words = self.list_words()
        return len(list_words)
    
    def is_empty(self):
        return len(self.root.children) == 0
    
    def clear(self):
        self.root.children = {}
                
    #TODO: delete(word: str)
                
            
    


            
        
        
        
            
    