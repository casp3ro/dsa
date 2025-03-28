
# O(n^2)
def insertion_sort(data:list)->list:
    for i in range(1, len(data)):
        current = data[i]
        j = i -1
        
        while current < data[j] and j>=0:
            # data[j+1] == current
            data[j+1] = data[j] # Shift larger to right
            j -=1 # Move left
            
        data[j+1] =  current #Insert element to correct position

    return data
    
    
    
    
def main():
    unsorted = [4932,2,32,-653,854,1,23,-5,-9,51,72,-11,9]
    sorted = insertion_sort(unsorted)
    print(sorted)
    
main()