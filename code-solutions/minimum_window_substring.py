def minimum_window_substring(s: str, t: str) -> str:
    """
    Finds the minimum window substring containing all characters of t using sliding window.
    
    Interview Tips:
    - Use sliding window with two pointers
    - Track character counts in both strings
    - Expand right until all characters found
    - Contract left while maintaining all characters
    - Key insight: track "have" vs "need" to know when window is valid
    
    Complexity: O(|s| + |t|) time, O(|s| + |t|) space
    """
    if t == '':
        return ''

    countT, window = {}, {}
    res, resLen = [-1, -1], float('infinity')
    l = 0

    for c in t:
        countT[c] = countT.get(c, 0) + 1

    have, need = 0, len(countT)

    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c, 0) + 1

        if c in countT and window[c] == countT[c]:
            have += 1

        while have == need:
            curr = (r - l + 1)
            if curr < resLen:
                res = [l, r]
                resLen = curr

            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1

    l, r = res

    if resLen == float("infinity"):
        return ''
    return s[l: r + 1]


def test_minimum_window_substring():
    """Test function that can be run from terminal."""
    # Test: s="ADOBECODEBANC", t="ABC" -> "BANC"
    s = "ADOBECODEBANC"
    t = "ABC"
    result = minimum_window_substring(s, t)
    print(f"String: '{s}', Target: '{t}'")
    print(f"Minimum window: '{result}'")


if __name__ == "__main__":
    test_minimum_window_substring()