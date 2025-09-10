def valid_palindrome(string: str) -> bool:
    """
    Checks if a string is a palindrome (ignoring non-alphanumeric characters).
    
    Interview Tips:
    - Use two pointers from both ends
    - Skip non-alphanumeric characters using isalnum()
    - Compare characters in lowercase
    - Move pointers inward after each comparison
    
    Complexity: O(n) time, O(1) space
    """
    l, r = 0, len(string) - 1
    
    while l < r:
        while l < r and not string[l].isalnum():
            l += 1
        
        while l < r and not string[r].isalnum():
            r -= 1
            
        if string[l].lower() != string[r].lower():
            return False
        
        l += 1
        r -= 1
        
    return True


def test_valid_palindrome():
    """Test function that can be run from terminal."""
    # Test: "A man, a plan, a canal: Panama" -> True
    test_str = "A man, a plan, a canal: Panama"
    result = valid_palindrome(test_str)
    print(f"String: '{test_str}'")
    print(f"Is palindrome: {result}")


if __name__ == "__main__":
    test_valid_palindrome()