class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def createLinkedList(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
    
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node
        new_node.prev = last_node
        
    def deleteAtEnd(self):
        if self.head is None:
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        if last_node.prev:
            last_node.prev.next = None
        else:
            self.head = None
        del last_node
        return
    
    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

def main():
    dll = DoublyLinkedList()
    dll.createLinkedList(10)
    print("Doubly Linked List after creating first node:")
    dll.insertAtEnd(20)
    dll.insertAtEnd(30)
    print("Doubly Linked List after inserting elements:")
    dll.printList()
    
    dll.deleteAtEnd()
    print("Doubly Linked List after deleting last element:")
    dll.printList()

if __name__ == "__main__":
    main()

        
        