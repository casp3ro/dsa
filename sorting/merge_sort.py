def merge_sort(data: list) -> list:
    """
    Sorts an array using the Merge Sort algorithm (Divide and Conquer).
    
    How it works:
    1. Divide: Split the array into two halves
    2. Conquer: Recursively sort both halves
    3. Combine: Merge the two sorted halves into a single sorted array
    
    Time Complexity: O(n log n) - always, regardless of input
    Space Complexity: O(n) - additional space for temporary arrays
    
    Advantages:
    - Guaranteed O(n log n) time complexity
    - Stable (maintains relative order of equal elements)
    - Predictable performance
    - Good for large datasets
    
    Disadvantages:
    - Requires O(n) extra space
    - Not in-place sorting
    """
    length = len(data)
    
    # Base case: array with 0 or 1 element is already sorted
    if length <= 1:
        return data

    # Divide: split array into two halves
    middle = length // 2
    left_half = data[:middle]
    right_half = data[middle:]
    
    # Conquer: recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combine: merge the two sorted halves
    return merge_arrays(left_sorted, right_sorted)


def merge_arrays(left: list, right: list) -> list:
    """
    Merges two sorted arrays into a single sorted array.
    
    How it works:
    1. Compare elements from both arrays
    2. Take the smaller element and add to result
    3. Continue until one array is exhausted
    4. Add remaining elements from the other array
    
    Time Complexity: O(n + m) where n, m are lengths of left and right arrays
    Space Complexity: O(n + m) for the result array
    """
    merged = []
    left_idx = right_idx = 0
    
    # Compare elements from both arrays and merge
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    
    # Add remaining elements from left array
    while left_idx < len(left):
        merged.append(left[left_idx])
        left_idx += 1
        
    # Add remaining elements from right array
    while right_idx < len(right):
        merged.append(right[right_idx])
        right_idx += 1
        
    return merged


def test_merge_sort():
    """Test function that can be run from terminal."""
    # Test case 1: Random unsorted array
    test_data = [4932, 2, 32, -653, 854, 1, 23, -5, -9, 51, 72, -11, 9]
    result = merge_sort(test_data.copy())
    print(f"Original: {test_data}")
    print(f"Sorted:   {result}")
    print(f"Is sorted: {result == sorted(test_data)}")
    print()
    
    # Test case 2: Already sorted array
    sorted_data = [1, 2, 3, 4, 5]
    result2 = merge_sort(sorted_data.copy())
    print(f"Already sorted: {sorted_data}")
    print(f"Result:        {result2}")
    print()
    
    # Test case 3: Reverse sorted array
    reverse_data = [5, 4, 3, 2, 1]
    result3 = merge_sort(reverse_data.copy())
    print(f"Reverse sorted: {reverse_data}")
    print(f"Result:         {result3}")
    print()
    
    # Test case 4: Array with duplicates (test stability)
    duplicate_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    result4 = merge_sort(duplicate_data.copy())
    print(f"With duplicates: {duplicate_data}")
    print(f"Result:          {result4}")
    print()
    
    # Test case 5: Single element
    single_data = [42]
    result5 = merge_sort(single_data.copy())
    print(f"Single element: {single_data}")
    print(f"Result:         {result5}")
    print()
    
    # Test case 6: Empty array
    empty_data = []
    result6 = merge_sort(empty_data.copy())
    print(f"Empty array: {empty_data}")
    print(f"Result:      {result6}")


if __name__ == "__main__":
    test_merge_sort()