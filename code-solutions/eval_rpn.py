def eval_rpn(tokens: list[str]) -> int:
    """
    Evaluates a Reverse Polish Notation expression using a stack.
    
    Interview Tips:
    - Use stack to store operands
    - When operator found, pop two operands and compute
    - Push result back to stack
    - Key insight: RPN processes operators after operands
    
    Complexity: O(n) time, O(n) space
    """
    if not tokens or len(tokens) == 0:
        return 0
    
    operators = ['+', '-', '*', '/']
    stack = []
    
    for token in tokens:
        if token in operators:
            num = stack.pop()
            base = stack.pop()
            
            if token == '+':
                stack.append(base + num)
            elif token == '-':
                stack.append(base - num)
            elif token == '*':
                stack.append(base * num)
            else:
                stack.append(int(base / num))
        else:
            stack.append(int(token))
    
    return stack[0]


def test_eval_rpn():
    """Test function that can be run from terminal."""
    # Test: ["2","1","+","3","*"] -> 9 ((2+1)*3)
    tokens = ["2", "1", "+", "3", "*"]
    result = eval_rpn(tokens)
    print(f"Tokens: {tokens}")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_eval_rpn()
            