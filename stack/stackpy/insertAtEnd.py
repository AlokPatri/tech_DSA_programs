class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def pop(self):
        if self.head is None:
            return
        temp = self.head
        if temp.next is None:
            self.head = None
            del temp
            return
        while temp.next and temp.next.next:
            temp = temp.next
        del temp.next
        temp.next = None
    
    def printStack(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

