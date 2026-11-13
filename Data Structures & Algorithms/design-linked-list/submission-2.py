class MyLinkedList:

    class ListNode:
        def __init__(self, val, next_node=None):
            self.val = val
            self.next = next_node
    
    def __init__(self):
        self.head = self.ListNode(0)
        self.tail = self.head
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head.next
        for i in range(index):
            current = current.next
        return current.val 
        

    def addAtHead(self, val: int) -> None:
        new_head = self.ListNode(val, self.head.next)
        self.head.next = new_head
        if self.size == 0:
            self.tail = new_head
        self.size += 1

        

    def addAtTail(self, val: int) -> None:
        new_tail = self.ListNode(val, None)
        self.tail.next = new_tail
        self.tail = new_tail
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        # Find the node BEFORE the insertion point
        previous = self.head
        for i in range(index):  # Loop only index times
            previous = previous.next
        
        # Insert the new node
        new_node = self.ListNode(val, previous.next)
        previous.next = new_node
        
        # Update tail if inserting at the end
        if index == self.size:
            self.tail = new_node
        
        self.size += 1

        

    def deleteAtIndex(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return 
        previous = self.head
        for i in range(index):
            previous = previous.next
        current = previous.next
        previous.next = current.next
        if current == self.tail:
            self.tail = previous
        self.size -= 1
        return 
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)