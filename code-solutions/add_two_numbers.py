class ListNode:
    """
    A node class for linked list implementation.
    
    Attributes:
        val: The value stored in the node
        next: Reference to the next node in the list
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Adds two numbers represented as linked lists where digits are stored in reverse order.
    
    Interview Tips:
    - Use dummy node to simplify edge cases
    - Handle carry properly (carry = val // 10, digit = val % 10)
    - Continue loop while l1 OR l2 OR carry exists
    - Move pointers only if they exist (l1 = l1.next if l1 else None)
    
    Complexity: O(max(m, n)) time, O(max(m, n)) space where m and n are the lengths of l1 and l2
    """
    dummy = ListNode()
    curr = dummy
    
    carry = 0
    
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        
        val = v1 + v2 + carry
        num = val % 10
        carry = val // 10
        
        curr.next = ListNode(num)
        curr = curr.next
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next


def print_linked_list(head: ListNode) -> str:
    """Helper function to convert linked list to string for display."""
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values)


def test_add_two_numbers():
    """Test function that can be run from terminal."""
    # Test: 342 + 465 = 807
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = add_two_numbers(l1, l2)
    print(f"342 + 465 = 807")
    print(f"l1: {print_linked_list(l1)}")
    print(f"l2: {print_linked_list(l2)}")
    print(f"Result: {print_linked_list(result)}")


if __name__ == "__main__":
    test_add_two_numbers()