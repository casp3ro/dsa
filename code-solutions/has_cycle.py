class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode) -> bool:
    """
    Detects if a linked list has a cycle using Floyd's cycle detection algorithm.
    
    Interview Tips:
    - Use two pointers: slow (1 step) and fast (2 steps)
    - If there's a cycle, fast will eventually catch up to slow
    - If fast reaches end, no cycle exists
    - Key insight: different speeds will meet in cycle
    
    Complexity: O(n) time, O(1) space
    """
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False


def test_has_cycle():
    """Test function that can be run from terminal."""
    # Test: Create a cycle in linked list
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head  # Create cycle
    
    result = has_cycle(head)
    print(f"Linked list has cycle: {result}")


if __name__ == "__main__":
    test_has_cycle()