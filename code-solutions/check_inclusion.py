def check_inclusion(s1: str, s2: str) -> bool:
    """
    Checks if s1's permutation is included in s2 using sliding window technique.
    
    Interview Tips:
    - Use sliding window of size len(s1)
    - Compare character frequency maps
    - Slide window by removing left char and adding right char
    - Key insight: permutation = same characters with same frequencies
    
    Complexity: O(n) time, O(1) space where n = len(s2)
    """
    s1_dict = {}
    window_dict = {}
    l = 0

    for s in s1:
        s1_dict[s] = s1_dict.get(s, 0) + 1

    for r in range(len(s2)):
        window_dict[s2[r]] = window_dict.get(s2[r], 0) + 1

        if r - l + 1 == len(s1):
            if s1_dict == window_dict:
                return True

            window_dict[s2[l]] -= 1
            if window_dict[s2[l]] == 0:
                del window_dict[s2[l]]
            l += 1

    return False


def test_check_inclusion():
    """Test function that can be run from terminal."""
    # Test: s1="ab", s2="eidbaooo" -> True (ba is permutation of ab)
    s1 = "ab"
    s2 = "eidbaooo"
    result = check_inclusion(s1, s2)
    print(f"s1: '{s1}', s2: '{s2}'")
    print(f"Permutation found: {result}")


if __name__ == "__main__":
    test_check_inclusion()