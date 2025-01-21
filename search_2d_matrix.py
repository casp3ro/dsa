def search_2d_matrix(matrix:list[list[int]],target:int)->bool:
    
    def binarySearch(arr:list[int],target:int)->bool:
        
        left, right = 0 , len(arr) -1
        
        while left<=right:
            middle = (left + right) // 2
            value = arr[middle]
            
            if target == value:
                return True
            if target > value:
                left = middle + 1
            else:
                right = middle - 1
        
        return False
    
    
    ROWS,COLS = len(matrix), len(matrix[0])
    
    top, bottom = 0, ROWS - 1
    
    while top<=bottom:
        
        middle = (top + bottom) //2
        middleArr = matrix[middle]
        
        if middleArr[0] <= target <= middleArr[COLS-1]:
            return binarySearch(middleArr,target)

        if middleArr[COLS-1] > target:
            bottom = middle - 1
        else:
            top = middle + 1
            
    return False
            
                