
special_char = '#'

def encode(strs: list[str]) -> str:
    """
    Encodes a list of strings into a single string with length prefixes.
    
    Interview Tips:
    - Use length + delimiter + string format
    - Length tells us how many characters to read
    - Delimiter separates length from actual string
    - Key insight: need to know where each string ends
    
    Complexity: O(n) time, O(1) space where n = total characters
    """
    output = ''
    
    for string in strs:
        length = str(len(string))
        output += length + special_char + string
    
    return output
        
    

def decode(s: str) -> list[str]:
    """
    Decodes a string back into a list of strings.
    
    Interview Tips:
    - Parse length before delimiter
    - Extract string of that length after delimiter
    - Move pointer to end of current string
    - Key insight: length tells us exactly how many chars to read
    
    Complexity: O(n) time, O(1) space where n = total characters
    """
    output = []
    i = 0
        
    while i < len(s):
        j = i
            
        while s[j] != special_char:
            j += 1
            
        length = int(s[i:j])
        start_index = j + 1
        end_index = start_index + length
        output.append(s[start_index:end_index])
        i = end_index
        
    return output


def test_encode_decode_strings():
    """Test function that can be run from terminal."""
    # Test: ["hello","world"] -> encode -> decode -> ["hello","world"]
    strs = ["hello", "world"]
    encoded = encode(strs)
    decoded = decode(encoded)
    print(f"Original: {strs}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")


if __name__ == "__main__":
    test_encode_decode_strings()