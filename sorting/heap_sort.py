# O(n log n)
def heapify(data:list, heap_size:int, index:int = 0) -> list:
    # indexes
    left = 2*index +1
    right = 2*index +2
    largest = index
    
    if left < heap_size and data[left] > data[largest]:
        largest = left
        
    if right < heap_size and data[right] > data[largest]:
        largest = right
        
    if largest != index:
        data[index], data[largest] = data[largest], data[index]
        heapify(data,heap_size,largest)


def build_max_heap(data:list) -> list:
     #?
    for i in range(len(data) // 2 -1, 0, -1):
        heapify(data,len(data), i)


def heap_sort(data:list) -> list:
    build_max_heap(data)
    #?
    for i in range(len(data) -1,-1,-1):
        data[0], data[i] = data[i],data[0]
        heapify(data, i)
        
        
    return data



def main():
      unsorted = [4932,2,32,-653,854,1,23,-5,-9,51,72,-11,9]
      sorted = heap_sort(unsorted)
      print(sorted)
      
main()