# O(n^2)
def selection_sort(data:list)->list:
    for i in range(len(data) -1):
        min_index = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_index]:
                min_index  = j
        if min_index !=i: 
            data[i], data[min_index] = data[min_index], data[i]
    
    return data


def main():
      unsorted = [4932,2,32,-653,854,1,23,-5,-9,51,72,-11,9]
      sorted = selection_sort(unsorted)
      print(sorted)
      
main()