def valid_parentheses(s:str)->bool:
    stack = []
    closed_open = {
        '}': '{',
        ']' : '[',
        ')' : '('
    }
    
    for char in s: 
        if char in closed_open:
            if len(stack) == 0:
                return False
            
            item = stack.pop()
            
            if item != closed_open[char]:
                return False
        else:
            stack.append(char)
    
    if len(stack) == 0:
        return True
    else:
        return False