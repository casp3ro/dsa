# O(n^2)
def bubble_sort(data:list) -> list :
    length = len(data)
    
    for i in range(length -1):
        swaped = False
        for j in range(length - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j +1], data[j]
                swaped = True
                
        if not swaped:
            break
        
    return data
        
    

def main():
    unsorted = [4932,2,32,-653,854,1,23,-5,-9,51,72,-11,9]
    sorted = bubble_sort(unsorted)
    print(sorted)
    
main()