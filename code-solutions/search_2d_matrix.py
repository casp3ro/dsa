def search_2d_matrix(matrix: list[list[int]], target: int) -> bool:
    """
    Searches for target in a 2D matrix using binary search on rows and columns.
    
    Interview Tips:
    - First binary search on rows to find potential row
    - Check if target is within row's range
    - Then binary search within that row
    - Key insight: matrix is sorted both row-wise and column-wise
    
    Complexity: O(log(m) + log(n)) time, O(1) space
    """
    def binarySearch(arr: list[int], target: int) -> bool:
        left, right = 0, len(arr) - 1
        
        while left <= right:
            middle = (left + right) // 2
            value = arr[middle]
            
            if target == value:
                return True
            if target > value:
                left = middle + 1
            else:
                right = middle - 1
        
        return False
    
    ROWS, COLS = len(matrix), len(matrix[0])
    top, bottom = 0, ROWS - 1
    
    while top <= bottom:
        middle = (top + bottom) // 2
        middleArr = matrix[middle]
        
        if middleArr[0] <= target <= middleArr[COLS - 1]:
            return binarySearch(middleArr, target)

        if middleArr[COLS - 1] > target:
            bottom = middle - 1
        else:
            top = middle + 1
            
    return False


def test_search_2d_matrix():
    """Test function that can be run from terminal."""
    # Test: Matrix [[1,4,7,11],[2,5,8,12],[3,6,9,16]], target=5 -> True
    matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]]
    target = 5
    result = search_2d_matrix(matrix, target)
    print(f"Matrix: {matrix}")
    print(f"Target: {target}")
    print(f"Found: {result}")


if __name__ == "__main__":
    test_search_2d_matrix()
            
                