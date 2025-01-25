class ListNode:
    def __init__(self,val= 0, next = None):
        self.val = val
        self.next = next
        

def remove_nth_from_end(head:ListNode, n:int)-> ListNode:
    dummy = ListNode(0,head)
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