
# O(n log n)

def merge_sort(data:list) -> list:
    length = len(data)
    
    if length == 1:
        return data

    middle = length // 2
    
    array_a = data[:middle]
    array_b = data[middle:]
    
    array_a = merge_sort(array_a)
    array_b = merge_sort(array_b)

    return sort_arrays(array_a,array_b)

def sort_arrays(array_a:list, array_b:list) -> list:
    sorted_array = []
    
    while array_a and array_b:
        if array_a[0] > array_b[0]:
            sorted_array.append(array_b[0])
            del array_b[0]
        else:
            sorted_array.append(array_a[0])
            del array_a[0]
    
    while array_a:
        sorted_array.append(array_a[0])
        del array_a[0]
        
    while array_b:
        sorted_array.append(array_b[0])
        del array_b[0]
        
        
    return sorted_array


def main():
    unsorted = [4932,2,32,-653,854,1,23,-5,-9,51,72,-11,9]
    sorted = merge_sort(unsorted)
    print(sorted)
    
main()