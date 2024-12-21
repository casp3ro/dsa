# O(n), O(1)

def valid_palindrome(string:str) -> bool:
    
    l,r = 0, len(string) - 1
    
    while l<r:
        
        while l<r and not string[l].isalnum():
            l+=1
        
        while l<r and not string[r].isalnum():
            r-=1
            
        if string[l].lower() != string[r].lower():
            return False
        
        l+=1
        r-=1
        
    
    return True