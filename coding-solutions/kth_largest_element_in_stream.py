import heapq

# Trick: Keep only K elements in the min heap. In the end, the K largest elements will be the first in the min heap because the others will be larger.
class KthLargestElementInStream:
    def __init__(self,k,nums):
        self.k, self.min_heap = k, nums
        heapq.heapify(self.min_heap)
     
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
    def add(self,val):
        heapq.heappush(self.min_heap,val)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]
        
        
        
        
