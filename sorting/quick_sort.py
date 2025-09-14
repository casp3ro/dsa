def quick_sort(data: list) -> list:
    """
    Sorts an array using the Quick Sort algorithm (Divide and Conquer).
    
    How it works:
    1. Choose a pivot element (middle element in this implementation)
    2. Partition: Rearrange array so elements < pivot are on left, > pivot on right
    3. Recursively sort the left and right subarrays
    4. Combine: The array is now sorted
    
    Time Complexity: 
    - Average Case: O(n log n) - good pivot selection
    - Best Case: O(n log n) - balanced partitions
    - Worst Case: O(n²) - when pivot is always min/max element
    
    Space Complexity: O(log n) - recursion stack depth
    
    Advantages:
    - Fast in practice (often faster than merge sort)
    - Sorts in place (with some implementations)
    - Cache-friendly
    
    Disadvantages:
    - Worst case O(n²) time complexity
    - Not stable (relative order of equal elements may change)
    - Performance depends on pivot selection
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(data) <= 1:
        return data
    
    # Choose pivot (middle element for better average performance)
    pivot_value = data[len(data) // 2]

    # Partition array around pivot
    smaller, middle, larger = partition(data, pivot_value)
    
    # Recursively sort smaller and larger parts, then combine
    return quick_sort(smaller) + middle + quick_sort(larger)


def partition(data: list, pivot_value: int) -> tuple[list, list, list]:
    """
    Partitions array into three parts based on pivot value.
    
    How it works:
    1. Create three lists: smaller, middle, larger
    2. Compare each element with pivot
    3. Place element in appropriate list based on comparison
    
    Time Complexity: O(n) - single pass through array
    Space Complexity: O(n) - for the three new lists
    
    Returns:
        tuple: (smaller_elements, equal_elements, larger_elements)
    """
    smaller = []
    middle = []
    larger = []
    
    # Partition elements based on pivot comparison
    for item in data:
        if item < pivot_value:
            smaller.append(item)
        elif item > pivot_value:
            larger.append(item)
        else:  # item == pivot_value
            middle.append(item)
            
    return smaller, middle, larger


def test_quick_sort():
    """Test function that can be run from terminal."""
    # Test case 1: Random unsorted array
    test_data = [4932, 2, 32, -653, 854, 1, 23, -5, -9, 51, 72, -11, 9]
    result = quick_sort(test_data.copy())
    print(f"Original: {test_data}")
    print(f"Sorted:   {result}")
    print(f"Is sorted: {result == sorted(test_data)}")
    print()
    
    # Test case 2: Already sorted array
    sorted_data = [1, 2, 3, 4, 5]
    result2 = quick_sort(sorted_data.copy())
    print(f"Already sorted: {sorted_data}")
    print(f"Result:        {result2}")
    print()
    
    # Test case 3: Reverse sorted array
    reverse_data = [5, 4, 3, 2, 1]
    result3 = quick_sort(reverse_data.copy())
    print(f"Reverse sorted: {reverse_data}")
    print(f"Result:         {result3}")
    print()
    
    # Test case 4: Array with duplicates
    duplicate_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    result4 = quick_sort(duplicate_data.copy())
    print(f"With duplicates: {duplicate_data}")
    print(f"Result:          {result4}")
    print()
    
    # Test case 5: Single element
    single_data = [42]
    result5 = quick_sort(single_data.copy())
    print(f"Single element: {single_data}")
    print(f"Result:         {result5}")
    print()
    
    # Test case 6: Empty array
    empty_data = []
    result6 = quick_sort(empty_data.copy())
    print(f"Empty array: {empty_data}")
    print(f"Result:      {result6}")
    print()
    
    # Test case 7: Array with all same elements
    same_data = [5, 5, 5, 5, 5]
    result7 = quick_sort(same_data.copy())
    print(f"All same elements: {same_data}")
    print(f"Result:            {result7}")


if __name__ == "__main__":
    test_quick_sort()