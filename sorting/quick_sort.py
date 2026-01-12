def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    pivot_index = i + 1
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return pivot_index

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if len(arr) == 0:
        return arr
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    return arr


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