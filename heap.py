import heapq

class MaxHeap:
    def __init__(self, values:list[int] = None):
        self.max_heap =  []
        if values:
            self.max_heap = [-i for i in values]
            heapq.heapify(self.max_heap)
            
    @property
    def is_empty(self)->bool:
        return len(self.max_heap) == 0
        
    def push(self, val:int):
        heapq.heappush(self.max_heap, -val)
        
    def pop(self)->int:
        if self.is_empty:
            return None
        val = heapq.heappop(self.max_heap)
        return -val
    
    def max_val(self)-> None|int:
        if  self.is_empty:
            return None
        return -self.max_heap[0]
    

    

    
max_heap = MaxHeap([50,20,30])

print(max_heap.max_val())
max_heap.pop()
print(max_heap.max_val())
max_heap.push(60)
print(max_heap.max_val())
