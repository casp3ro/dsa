def valid_parentheses(s: str) -> bool:
    """
    Checks if a string has valid parentheses, brackets, and braces.
    
    Interview Tips:
    - Use stack to track opening brackets
    - Create mapping of closing to opening brackets
    - If closing bracket, check if stack is empty or doesn't match
    - Final check: stack must be empty for valid string
    
    Complexity: O(n) time, O(n) space
    """
    stack = []
    closed_open = {
        '}': '{',
        ']': '[',
        ')': '('
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
    
    return len(stack) == 0


def test_valid_parentheses():
    """Test function that can be run from terminal."""
    # Test: "()[]{}" -> True
    test_str = "()[]{}"
    result = valid_parentheses(test_str)
    print(f"String: '{test_str}'")
    print(f"Valid: {result}")


if __name__ == "__main__":
    test_valid_parentheses()