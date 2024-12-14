def binary_search(data: list, target: int) -> int:
    left, right = 0, len(data) - 1
    
    while left <= right:
        middle = (left + right) // 2
        value = data[middle]
        
        if target == value:
            return middle
        elif value < target:
            left = middle + 1
        else:
            right = middle - 1
    
    return None
