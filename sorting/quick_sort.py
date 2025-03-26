
# avg:O(n log n) worst: O(n^2)

def quick_sort(data:list) -> list:
    if len(data) <=1:
        return data
    
    pivot_value = data[len(data) //2]

    smaller,middle,higher = partition(data,pivot_value)
    
    return quick_sort(smaller) + middle + quick_sort(higher)

def partition(data, pivot_value):
    smaller = []
    middle = []
    higher = []
    
    for item in data:
        if item > pivot_value:
            higher.append(item)
        elif item < pivot_value:
            smaller.append(item)
        else:
            middle.append(item)
            
    return (smaller,middle,higher)
    
    

def main():
      unsorted = [4932,2,32,-653,854,1,23,-5,-9,51,72,-11,9]
      sorted = quick_sort(unsorted)
      print(sorted)
      
main()