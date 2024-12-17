
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
# Time&Space: O(n) 

def copy_linked_list_with_random_pointer(head: 'Optional[Node]') -> 'Optional[Node]':
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