class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
        


def merge_two_lists(list1:ListNode, list2:ListNode)->ListNode:
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
            