class LinkedList:

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
        return current.val if current else -1

    def insertHead(self, val: int) -> None:
        new_head = self.ListNode(val, self.head.next)
        self.head.next = new_head
        if self.size == 0:
            self.tail = new_head
        self.size += 1

    def insertTail(self, val: int) -> None:
        new_tail = self.ListNode(val, None)
        self.tail.next = new_tail
        self.tail = new_tail
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        previous = self.head
        for i in range(index):
            previous = previous.next
        current = previous.next
        previous.next = current.next
        if current == self.tail:
            self.tail = previous
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        current = self.head.next
        array = []
        while current:
            array.append(current.val)
            current = current.next
        return array