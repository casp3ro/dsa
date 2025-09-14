def bubble_sort(data: list) -> list:
    """
    Sorts an array using the Bubble Sort algorithm.
    
    How it works:
    1. Compare adjacent elements and swap if they are in wrong order
    2. Repeat for each pair of adjacent elements
    3. After each pass, the largest element "bubbles" to the end
    4. Continue until no more swaps are needed (optimization)
    
    Time Complexity: O(n²) - nested loops, worst case
    Space Complexity: O(1) - sorts in place
    
    Best Case: O(n) - when array is already sorted (with optimization)
    Worst Case: O(n²) - when array is sorted in reverse order
    """
    length = len(data)
    
    # Outer loop: number of passes through the array
    for i in range(length - 1):
        swapped = False  # Optimization: track if any swaps occurred
        
        # Inner loop: compare adjacent elements
        # After each pass, the largest element is in its correct position
        for j in range(length - i - 1):
            if data[j] > data[j + 1]:
                # Swap elements if they are in wrong order
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                
        # If no swaps occurred, array is already sorted
        if not swapped:
            break
        
    return data


def test_bubble_sort():
    """Test function that can be run from terminal."""
    # Test case 1: Random unsorted array
    test_data = [4932, 2, 32, -653, 854, 1, 23, -5, -9, 51, 72, -11, 9]
    result = bubble_sort(test_data.copy())
    print(f"Original: {test_data}")
    print(f"Sorted:   {result}")
    print(f"Is sorted: {result == sorted(test_data)}")
    print()
    
    # Test case 2: Already sorted array (best case)
    sorted_data = [1, 2, 3, 4, 5]
    result2 = bubble_sort(sorted_data.copy())
    print(f"Already sorted: {sorted_data}")
    print(f"Result:        {result2}")
    print()
    
    # Test case 3: Reverse sorted array (worst case)
    reverse_data = [5, 4, 3, 2, 1]
    result3 = bubble_sort(reverse_data.copy())
    print(f"Reverse sorted: {reverse_data}")
    print(f"Result:         {result3}")


if __name__ == "__main__":
    test_bubble_sort()