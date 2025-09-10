class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Merges two sorted linked lists into one sorted linked list.
    
    Interview Tips:
    - Use dummy node to simplify edge cases
    - Compare values and link smaller node
    - Move pointer of the list that was used
    - Append remaining nodes from either list
    
    Complexity: O(n + m) time, O(1) space where n and m are list lengths
    """
    if not list1 and not list2:
        return None
    
    dummy = ListNode()
    curr = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    
    if list1:
        curr.next = list1
    
    if list2:
        curr.next = list2
        
    return dummy.next


def print_linked_list(head: ListNode) -> str:
    """Helper function to convert linked list to string for display."""
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values)


def test_merge_two_lists():
    """Test function that can be run from terminal."""
    # Test: [1,2,4] + [1,3,4] -> [1,1,2,3,4,4]
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    result = merge_two_lists(list1, list2)
    print(f"List1: {print_linked_list(list1)}")
    print(f"List2: {print_linked_list(list2)}")
    print(f"Merged: {print_linked_list(result)}")


if __name__ == "__main__":
    test_merge_two_lists()
            