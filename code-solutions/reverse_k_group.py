class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head: ListNode, k: int) -> ListNode:
    """
    Reverses nodes in k-group chunks in a linked list.
    
    Interview Tips:
    - Use helper function to get kth node
    - Reverse each group of k nodes
    - Connect groups properly
    - Key insight: reverse each group and connect to previous group
    
    Complexity: O(n) time, O(1) space
    """
    def getKth(head: ListNode, k: int):
        curr = head
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
    dummy = ListNode(0, head)
    group_prev = dummy
    
    while True:
        kth = getKth(group_prev, k)
        if not kth:
            break
        
        group_next = kth.next
        
        curr, prev = group_prev.next, kth.next
        while curr != group_next:
            old_next = curr.next
            curr.next = prev
            prev = curr
            curr = old_next
            
        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp
        
    return dummy.next


def print_linked_list(head: ListNode) -> str:
    """Helper function to convert linked list to string for display."""
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values)


def test_reverse_k_group():
    """Test function that can be run from terminal."""
    # Test: [1,2,3,4,5], k=2 -> [2,1,4,3,5]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 2
    result = reverse_k_group(head, k)
    print(f"Original: {print_linked_list(head)}")
    print(f"Reverse in groups of {k}: {print_linked_list(result)}")


if __name__ == "__main__":
    test_reverse_k_group()