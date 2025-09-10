import heapq


class FindMedianFromDataStream:
    """
    Finds median from a data stream using two heaps (small max-heap, large min-heap).
    
    Interview Tips:
    - Use small heap (max-heap) for smaller half, large heap (min-heap) for larger half
    - Keep heaps balanced: |len(small) - len(large)| <= 1
    - Median = top of larger heap or average of both tops
    - Key insight: two heaps maintain sorted order efficiently
    
    Complexity: O(log n) add, O(1) find median
    """
    def __init__(self):
        self.large = []  # min heap
        self.small = []  # max heap
        
    def add_num(self, num):
        heapq.heappush(self.small, num * -1)
        
        if self.small and self.large and (self.small[0] * -1) > self.large[0]:
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
            return self.small[0] * -1
     
        if len(self.large) > len(self.small):
            return self.large[0] 

        median = (self.large[0] + (self.small[0] * -1)) / 2
        return median


def test_find_median_from_data_stream():
    """Test function that can be run from terminal."""
    # Test: Add [1,2,3] -> median = 2
    median_finder = FindMedianFromDataStream()
    median_finder.add_num(1)
    median_finder.add_num(2)
    median_finder.add_num(3)
    result = median_finder.find_median()
    print(f"Numbers added: [1,2,3]")
    print(f"Median: {result}")


if __name__ == "__main__":
    test_find_median_from_data_stream() 
        
         