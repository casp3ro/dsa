class ListNode:
    def __init__(self,val= 0, next= None):
        self.val = 0
        self.next = next
        

def reverse_k_group(head:ListNode,k:int)->ListNode:
    def getKth(head:ListNode,k:int):
        curr = head
        while curr and k > 0:
            curr = curr.next
            k-=1
        return curr
    
    dummy = ListNode(0,head)
    group_prev= dummy
    
    while True:
        kth = getKth(group_prev,k)
        if not kth:
            break
        
        group_next = kth.next
        
        curr, prev = group_prev.next, kth.next
        while curr !=group_next:
            old_next = curr.next
            curr.next = prev
            prev = curr
            curr  = old_next
            
        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp
        
    
    return dummy.next