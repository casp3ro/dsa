
special_char = '#'

def encode(strs: list[str]) -> str:
    output = ''
    
    for string in strs:
        length = str(len(string))
        output += length + special_char + string
    
    return output
        
    

def decode(s: str) -> list[str]:
    output = []
        
    i = 0
        
    while i < len(s):
        j = i
            
        while s[j] != special_char:
            j+=1
            
        length = int(s[i:j])
        start_index = j+1
        end_index = start_index + length
        output.append(s[start_index:end_index])
        i = end_index
        
    return output 

    