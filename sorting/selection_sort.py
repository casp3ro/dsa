def selection_sort(data: list) -> list:
    """
    Sorts an array using the Selection Sort algorithm.
    
    How it works:
    1. Find the minimum element in the unsorted portion
    2. Swap it with the first element of the unsorted portion
    3. Move the boundary of sorted portion one position to the right
    4. Repeat until the entire array is sorted
    
    Time Complexity: O(n²) - always, regardless of input
    Space Complexity: O(1) - sorts in place
    
    Best Case: O(n²) - even if array is sorted, we still check all elements
    Worst Case: O(n²) - same as best case
    
    Advantages:
    - Simple implementation
    - Sorts in place
    - Makes minimum number of swaps (O(n) swaps)
    - Not affected by input distribution
    
    Disadvantages:
    - Always O(n²) time complexity
    - Not stable (relative order of equal elements may change)
    - Not efficient for large datasets
    """
    # Iterate through the array
    for i in range(len(data) - 1):
        min_index = i  # Assume first element is minimum
        
        # Find the minimum element in remaining unsorted array
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
                
        # Swap the found minimum element with the first element
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
    
    return data


def test_selection_sort():
    """Test function that can be run from terminal."""
    # Test case 1: Random unsorted array
    test_data = [4932, 2, 32, -653, 854, 1, 23, -5, -9, 51, 72, -11, 9]
    result = selection_sort(test_data.copy())
    print(f"Original: {test_data}")
    print(f"Sorted:   {result}")
    print(f"Is sorted: {result == sorted(test_data)}")
    print()
    
    # Test case 2: Already sorted array
    sorted_data = [1, 2, 3, 4, 5]
    result2 = selection_sort(sorted_data.copy())
    print(f"Already sorted: {sorted_data}")
    print(f"Result:        {result2}")
    print()
    
    # Test case 3: Reverse sorted array
    reverse_data = [5, 4, 3, 2, 1]
    result3 = selection_sort(reverse_data.copy())
    print(f"Reverse sorted: {reverse_data}")
    print(f"Result:         {result3}")
    print()
    
    # Test case 4: Array with duplicates
    duplicate_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    result4 = selection_sort(duplicate_data.copy())
    print(f"With duplicates: {duplicate_data}")
    print(f"Result:          {result4}")
    print()
    
    # Test case 5: Single element
    single_data = [42]
    result5 = selection_sort(single_data.copy())
    print(f"Single element: {single_data}")
    print(f"Result:         {result5}")
    print()
    
    # Test case 6: Empty array
    empty_data = []
    result6 = selection_sort(empty_data.copy())
    print(f"Empty array: {empty_data}")
    print(f"Result:      {result6}")
    print()
    
    # Test case 7: Array with all same elements
    same_data = [5, 5, 5, 5, 5]
    result7 = selection_sort(same_data.copy())
    print(f"All same elements: {same_data}")
    print(f"Result:            {result7}")


if __name__ == "__main__":
    test_selection_sort()