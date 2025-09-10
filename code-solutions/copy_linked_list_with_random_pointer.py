
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_linked_list_with_random_pointer(head: 'Optional[Node]') -> 'Optional[Node]':
    """
    Creates a deep copy of a linked list with random pointers.
    
    Interview Tips:
    - Use hash map to map old nodes to new nodes
    - First pass: create all new nodes
    - Second pass: connect next and random pointers
    - Key insight: need to map old nodes to new nodes for random pointers
    
    Complexity: O(n) time, O(n) space
    """
    if not head:
        return None

    oldToNew = {}
    current = head
    
    while current:
        oldToNew[current] = Node(current.val)
        current = current.next

    current = head
    while current:
        if current.next:
            oldToNew[current].next = oldToNew[current.next]
        if current.random:
            oldToNew[current].random = oldToNew[current.random]
        current = current.next

    return oldToNew[head]


def test_copy_linked_list_with_random_pointer():
    """Test function that can be run from terminal."""
    # Test: Create a linked list with random pointers
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node1.random = node2
    node2.random = node2
    
    copied = copy_linked_list_with_random_pointer(node1)
    print(f"Original list copied successfully: {copied is not None}")
    print(f"Copied head value: {copied.val if copied else None}")


if __name__ == "__main__":
    test_copy_linked_list_with_random_pointer()