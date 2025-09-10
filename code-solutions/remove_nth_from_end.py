class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    """
    Removes the nth node from the end of a linked list using two pointers.
    
    Interview Tips:
    - Use dummy node to handle edge cases
    - Move right pointer n steps ahead
    - Move both pointers until right reaches end
    - Remove node by updating left.next
    - Key insight: gap of n between left and right pointers
    
    Complexity: O(n) time, O(1) space
    """
    dummy = ListNode(0, head)
    left = dummy
    right = dummy
    
    for _ in range(n):
        if right.next:
            right = right.next
            
    while right.next:
        left = left.next
        right = right.next
    
    left.next = left.next.next
    
    return dummy.next


def print_linked_list(head: ListNode) -> str:
    """Helper function to convert linked list to string for display."""
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values)


def test_remove_nth_from_end():
    """Test function that can be run from terminal."""
    # Test: [1,2,3,4,5], n=2 -> [1,2,3,5]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    result = remove_nth_from_end(head, n)
    print(f"Original: {print_linked_list(head)}")
    print(f"Remove {n}th from end: {print_linked_list(result)}")


if __name__ == "__main__":
    test_remove_nth_from_end()