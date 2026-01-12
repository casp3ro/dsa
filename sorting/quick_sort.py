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

def quick_sort(arr, low, high):

    if len(arr) <= 1:
        return arr
    
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)



def test_quick_sort():
    """Test function that can be run from terminal."""
    # Test case 1: Random unsorted array
    test_data = [4932, 2, 32, -653, 854, 1, 23, -5, -9, 51, 72, -11, 9]
    copy_test_data = test_data[:]
    quick_sort(copy_test_data, 0 , len(copy_test_data) - 1)
    print(f"Original: {test_data}")
    print(f"Sorted:   {copy_test_data}")
    print(f"Is sorted: {copy_test_data == sorted(test_data)}")
    print()
    
    # Test case 2: Already sorted array
    sorted_data = [1, 2, 3, 4, 5]
    copy_sorted_data = sorted_data[:]
    quick_sort(copy_sorted_data, 0 , len(copy_sorted_data) - 1)
    print(f"Already sorted: {sorted_data}")
    print(f"Result:        {copy_sorted_data}")
    print()
    
    # Test case 3: Reverse sorted array
    reverse_data = [5, 4, 3, 2, 1]
    copy_reverse_data = reverse_data[:]
    quick_sort(copy_reverse_data, 0 , len(copy_reverse_data) - 1)
    print(f"Reverse sorted: {reverse_data}")
    print(f"Result:         {copy_reverse_data}")
    print()
    
    # Test case 4: Array with duplicates
    duplicate_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    copy_duplicate_data = duplicate_data[:]
    quick_sort(copy_duplicate_data, 0 , len(copy_duplicate_data) - 1)
    print(f"With duplicates: {duplicate_data}")
    print(f"Result:          {copy_duplicate_data}")
    print()
    
    # Test case 5: Single element
    single_data = [42]
    copy_single_data = single_data[:]
    quick_sort(copy_single_data, 0 , len(copy_single_data) - 1)
    print(f"Single element: {single_data}")
    print(f"Result:         {copy_single_data}")
    print()
    
    # Test case 6: Empty array
    empty_data = []
    copy_empty_data = empty_data[:]
    quick_sort(copy_empty_data, 0 , len(copy_empty_data) - 1)
    print(f"Empty array: {empty_data}")
    print(f"Result:      {copy_empty_data}")
    print()
    
    # Test case 7: Array with all same elements
    same_data = [5, 5, 5, 5, 5]
    copy_same_data = same_data[:]
    quick_sort(copy_same_data, 0 , len(copy_same_data) - 1)
    print(f"All same elements: {same_data}")
    print(f"Result:            {copy_same_data}")


if __name__ == "__main__":
    test_quick_sort()