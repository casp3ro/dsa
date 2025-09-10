
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: list[ListNode]) -> ListNode:
    """
    Merges k sorted linked lists using divide and conquer approach.
    
    Interview Tips:
    - Use divide and conquer: merge pairs of lists iteratively
    - Each iteration reduces number of lists by half
    - Use existing merge two lists function
    - Key insight: merge in pairs rather than one by one
    
    Complexity: O(n log k) time, O(1) space where n = total nodes
    """
    if len(lists) == 0:
        return None
    
    def mergeList(l1: ListNode, l2: ListNode):
        dummy = ListNode()
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        return dummy.next
    
    while len(lists) > 1:
        mergedLists = []
        
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 in range(len(lists)) else None
            mergedLists.append(mergeList(l1, l2))
            
        lists = mergedLists
        
    return lists[0]


def print_linked_list(head: ListNode) -> str:
    """Helper function to convert linked list to string for display."""
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values)


def test_merge_k_lists():
    """Test function that can be run from terminal."""
    # Test: Merge [[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))
    
    lists = [list1, list2, list3]
    result = merge_k_lists(lists)
    print(f"Lists: [[1,4,5],[1,3,4],[2,6]]")
    print(f"Merged: {print_linked_list(result)}")


if __name__ == "__main__":
    test_merge_k_lists()