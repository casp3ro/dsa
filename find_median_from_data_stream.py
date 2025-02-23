import heapq


class FindMedianFromDataStream:
    def __init__(self):
        self.large = [] #min heap
        self.small = [] #max heap
        
    def add_num(self,num):
        heapq.heappush(self.small,num *-1)
        
        if self.small and self.large and (self.small[0] *-1) > self.large[0]:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, val * -1)
            
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)
        
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small) 
            heapq.heappush(self.large, val * -1)   
        
    def find_median(self):
        if len(self.small) > len(self.large):
            return self.small[0] *-1
     
        if len(self.large) > len(self.small):
            return self.large[0] 

        median = ( self.large[0] + (self.small[0] * -1) )/2
        return median 
        
         