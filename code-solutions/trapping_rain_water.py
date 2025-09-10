def trapping_rain_water(height: list[int]) -> int:
    """
    Calculates the amount of rainwater that can be trapped between bars.
    
    Interview Tips:
    - Use two pointers from both ends
    - Track max heights from left and right
    - Water trapped = min(max_left, max_right) - current_height
    - Move pointer with smaller max height
    - Key insight: water level is limited by smaller of two max heights
    
    Complexity: O(n) time, O(1) space
    """
    if not height:
        return 0
    
    output = 0
    l, r = 0, len(height) - 1
    max_left, max_right = height[l], height[r]
    
    while l < r:
        if max_left < max_right:
            l += 1
            max_left = max(max_left, height[l])
            output += max_left - height[l]
        else:
            r -= 1
            max_right = max(max_right, height[r])
            output += max_right - height[r]
            
    return output


def test_trapping_rain_water():
    """Test function that can be run from terminal."""
    # Test: [0,1,0,2,1,0,1,3,2,1,2,1] -> 6 units of water
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = trapping_rain_water(height)
    print(f"Heights: {height}")
    print(f"Water trapped: {result}")


if __name__ == "__main__":
    test_trapping_rain_water()