def eval_rpn(tokens:list[str])->int:
    if not tokens or len(tokens) == 0:
        return 0
    
    operators = ['+', '-', '*', '/']
    stack = []
    
    for token in tokens:
        
        if token in operators:
            num = stack.pop()
            base = stack.pop()
            
            if token == '+':
                stack.append(base+num)
            elif token =='-':
                stack.append(base-num)
            elif token == '*':
                stack.append(base*num)
            else:
                stack.append(int(base/num))
        else:
            stack.append(int(token))
    
    
    return stack[0]
            