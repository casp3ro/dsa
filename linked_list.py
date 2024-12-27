#  TODO
#  value_n_from_end(n) - returns the value of the node at the nth position from the end of the list
#  reverse() - reverses the list
#  remove_value(value) - removes the first item in the list with this value


class Node:
    def __init__(self,value:int,next: 'Node'= None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head
        if head is not None:
            self.size = 1
        else:
            self.size = 0

    # bool returns true if empty
    def empty(self):
        return self.head is None
    
    # returns the value of the nth item (starting at 0 for first)
    def value_at(self,index:int):
        if index < 0 or index >= self.size:
            return None
        
        curr_index = 0
        curr = self.head
        
        while curr is not None:
            if curr_index == index:
                return curr.value
            
            curr = curr.next
            curr_index += 1
        
        return None
        
    # adds an item to the front of the list   
    def push_front(self,value:int):
        new_head = Node(value)
        prev_head  = self.head
        
        self.head = new_head
        self.head.next = prev_head
        
        self.size +=1
    
    # adds an item at the end
    def push_back(self,value:int): #no tail pointer in this case 
        new_last_node = Node(value)
        
        if self.empty():
            self.head  = new_last_node
        else:
            last_node = self.head
            
            while last_node.next:
                last_node = last_node.next
            
            last_node.next = new_last_node
            
        self.size +=1
        
    # removes end item and returns its value    
    def pop_back(self):
        if self.empty():
            return None
        
        last = self.head
        pre_last = None
        
        if self.size == 1:
            self.head = None
            self.size -=1
            return last.value
        
        while last.next is not None:
            pre_last = last
            last = last.next

        self.size -=1
        pre_last.next = None
            
        return last.value
    
    # remove the front item and return its value
    def pop_front(self):
        if self.empty():
            return None
        
        first = self.head
        new_first = self.head.next
        
        self.head = new_first
        
        self.size -=1
        
        return first.value
    
    # get the value of the front item
    def front(self):
        if self.empty():
            return None
        
        return self.head.value
    
    # get the value of the end item
    def back(self):
        
        curr = self.head
        
        while curr.next is not None:
            curr = curr.next
            
        return curr.value
    
    # insert value at index, so the current item at that index is pointed to by the new item at the index
    def insert(self,index,value):
        if self.empty() or index >= self.size or index < 0:
            return None
        
        curr = self.head
        counter = 0
        
        if index == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            
            self.size +=1
            return
            
        
        while counter < index - 1:
            curr = curr.next
            counter +=1
            
             
        new_node = Node(value)
        new_node.next = curr.next
        curr.next = new_node
        
        self.size +=1
        
    # removes node at given index    
    def erase(self,index):
        if index < 0 or index >= self.size or self.empty():
            return None
        
        curr = self.head
        counter = 0
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
            
        while counter < index -1:
            curr = curr.next
            counter +=1
            
        curr.next = curr.next.next
        self.size -= 1
            
        



