import heapq


class KthLargestElementInStream:
    """
    Finds kth largest element in a stream using a min heap of size k.
    
    Interview Tips:
    - Keep only k elements in min heap
    - When heap size > k, remove smallest element
    - Root of min heap is always kth largest
    - Key insight: min heap of size k keeps k largest elements
    
    Complexity: O(log k) add, O(1) find kth largest
    """
    def __init__(self, k, nums):
        self.k, self.min_heap = k, nums
        heapq.heapify(self.min_heap)
     
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
    def add(self, val):
        heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]


def test_kth_largest_element_in_stream():
    """Test function that can be run from terminal."""
    # Test: k=3, initial=[4,5,8,2], add 3,5,10,9,4
    kth_largest = KthLargestElementInStream(3, [4, 5, 8, 2])
    result1 = kth_largest.add(3)  # returns 4
    result2 = kth_largest.add(5)  # returns 5
    result3 = kth_largest.add(10)  # returns 5
    print(f"k=3, initial=[4,5,8,2]")
    print(f"Add 3 -> {result1}")
    print(f"Add 5 -> {result2}")
    print(f"Add 10 -> {result3}")


if __name__ == "__main__":
    test_kth_largest_element_in_stream()
        
        
        
        
