def heapify(data: list, heap_size: int, index: int = 0) -> None:
    """
    Maintains the heap property for a subtree rooted at index.
    
    How it works:
    1. Find the largest among root, left child, and right child
    2. If root is not the largest, swap with the largest child
    3. Recursively heapify the affected subtree
    
    Time Complexity: O(log n) - height of the tree
    Space Complexity: O(log n) - recursion stack
    """
    # Calculate indices of left and right children
    left = 2 * index + 1
    right = 2 * index + 2
    largest = index
    
    # Check if left child is larger than root
    if left < heap_size and data[left] > data[largest]:
        largest = left
        
    # Check if right child is larger than current largest
    if right < heap_size and data[right] > data[largest]:
        largest = right
        
    # If largest is not root, swap and continue heapifying
    if largest != index:
        data[index], data[largest] = data[largest], data[index]
        heapify(data, heap_size, largest)


def build_max_heap(data: list) -> None:
    """
    Builds a max heap from an unsorted array.
    
    How it works:
    1. Start from the last non-leaf node (parent of last element)
    2. Heapify each node from bottom to top
    3. This ensures the entire array satisfies heap property
    
    Time Complexity: O(n) - amortized analysis
    Space Complexity: O(log n) - recursion stack
    """
    # Start from the last non-leaf node and work backwards
    for i in range(len(data) // 2 - 1, -1, -1):
        heapify(data, len(data), i)


def heap_sort(data: list) -> list:
    """
    Sorts an array using the Heap Sort algorithm.
    
    How it works:
    1. Build a max heap from the input array
    2. Repeatedly extract the maximum element (root)
    3. Place it at the end of the array
    4. Reduce heap size and heapify the remaining elements
    
    Time Complexity: O(n log n) - build heap O(n) + n extractions O(n log n)
    Space Complexity: O(1) - sorts in place (excluding recursion stack)
    
    Advantages:
    - Guaranteed O(n log n) time complexity
    - Sorts in place
    - Not stable (relative order of equal elements may change)
    """
    # Build max heap
    build_max_heap(data)
    
    # Extract elements one by one
    for i in range(len(data) - 1, 0, -1):
        # Move current root to end
        data[0], data[i] = data[i], data[0]
        # Heapify the reduced heap
        heapify(data, i)
        
    return data


def test_heap_sort():
    """Test function that can be run from terminal."""
    # Test case 1: Random unsorted array
    test_data = [4932, 2, 32, -653, 854, 1, 23, -5, -9, 51, 72, -11, 9]
    result = heap_sort(test_data.copy())
    print(f"Original: {test_data}")
    print(f"Sorted:   {result}")
    print(f"Is sorted: {result == sorted(test_data)}")
    print()
    
    # Test case 2: Already sorted array
    sorted_data = [1, 2, 3, 4, 5]
    result2 = heap_sort(sorted_data.copy())
    print(f"Already sorted: {sorted_data}")
    print(f"Result:        {result2}")
    print()
    
    # Test case 3: Reverse sorted array
    reverse_data = [5, 4, 3, 2, 1]
    result3 = heap_sort(reverse_data.copy())
    print(f"Reverse sorted: {reverse_data}")
    print(f"Result:         {result3}")
    print()
    
    # Test case 4: Array with duplicates
    duplicate_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    result4 = heap_sort(duplicate_data.copy())
    print(f"With duplicates: {duplicate_data}")
    print(f"Result:          {result4}")


if __name__ == "__main__":
    test_heap_sort()