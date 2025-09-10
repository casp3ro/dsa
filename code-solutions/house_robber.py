def house_robber(house_values: list) -> int:
    """
    Finds maximum money that can be robbed from houses without robbing adjacent houses.
    
    Interview Tips:
    - Use dynamic programming with two variables (previous, current)
    - At each house: rob it (previous + current) or skip it (current)
    - Update previous = current, current = max(rob, skip)
    - Key insight: can't rob adjacent houses, so track previous decision
    
    Complexity: O(n) time, O(1) space
    """
    if not house_values:
        return 0

    if len(house_values) == 1:
        return house_values[0]
    
    previous, current = 0, 0

    for value in house_values:
        temp = max(previous + value, current)
        previous = current
        current = temp

    return current


def test_house_robber():
    """Test function that can be run from terminal."""
    # Test: [2,7,9,3,1] -> max = 12 (rob houses 0, 2, 4)
    houses = [2, 7, 9, 3, 1]
    result = house_robber(houses)
    print(f"Houses: {houses}")
    print(f"Max money: {result}")


if __name__ == "__main__":
    test_house_robber()