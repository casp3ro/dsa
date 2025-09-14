def insertion_sort(data: list) -> list:
    """
    Sorts an array using the Insertion Sort algorithm.
    
    How it works:
    1. Start with the second element (index 1)
    2. For each element, compare it with elements to its left
    3. Shift larger elements one position to the right
    4. Insert the current element in its correct position
    5. Repeat until all elements are processed
    
    Time Complexity: O(n²) - nested loops in worst case
    Space Complexity: O(1) - sorts in place
    
    Best Case: O(n) - when array is already sorted
    Worst Case: O(n²) - when array is sorted in reverse order
    
    Advantages:
    - Simple implementation
    - Efficient for small datasets
    - Stable (maintains relative order of equal elements)
    - Online algorithm (can sort as it receives data)
    """
    # Start from the second element (index 1)
    for i in range(1, len(data)):
        current = data[i]  # Element to be inserted
        j = i - 1  # Index of the last element in sorted portion
        
        # Shift elements greater than current one position to the right
        while current < data[j] and j >= 0:
            data[j + 1] = data[j]  # Shift larger element to the right
            j -= 1  # Move to the previous element
            
        # Insert current element in its correct position
        data[j + 1] = current

    return data


def test_insertion_sort():
    """Test function that can be run from terminal."""
    # Test case 1: Random unsorted array
    test_data = [4932, 2, 32, -653, 854, 1, 23, -5, -9, 51, 72, -11, 9]
    result = insertion_sort(test_data.copy())
    print(f"Original: {test_data}")
    print(f"Sorted:   {result}")
    print(f"Is sorted: {result == sorted(test_data)}")
    print()
    
    # Test case 2: Already sorted array (best case)
    sorted_data = [1, 2, 3, 4, 5]
    result2 = insertion_sort(sorted_data.copy())
    print(f"Already sorted: {sorted_data}")
    print(f"Result:        {result2}")
    print()
    
    # Test case 3: Reverse sorted array (worst case)
    reverse_data = [5, 4, 3, 2, 1]
    result3 = insertion_sort(reverse_data.copy())
    print(f"Reverse sorted: {reverse_data}")
    print(f"Result:         {result3}")
    print()
    
    # Test case 4: Array with duplicates (test stability)
    duplicate_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    result4 = insertion_sort(duplicate_data.copy())
    print(f"With duplicates: {duplicate_data}")
    print(f"Result:          {result4}")
    print()
    
    # Test case 5: Single element
    single_data = [42]
    result5 = insertion_sort(single_data.copy())
    print(f"Single element: {single_data}")
    print(f"Result:         {result5}")


if __name__ == "__main__":
    test_insertion_sort()