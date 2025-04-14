#traverse from 1 to position - 1
#delete node = temp.next
#temp.next = delete.next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_list(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
    
    def deleteAtPosition(self, position):
        if self.head is None:
            print("list is empty")
            return
        if position == 1:
            if self.head.next is None:
                self.head = None
                return
            temp = self.head
            self.head = self.head.next
            del temp
            return
        current = self.head
        for _ in range(1, position - 1):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next

        if current is None or current.next is None:
            print("Position out of bounds")
            return
        delete_node = current.next
        current.next = delete_node.next
        del delete_node
        return
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

def main():
    linked_list = LinkedList()
    linked_list.create_list(1)
    linked_list.create_list(2)
    linked_list.create_list(3)
    linked_list.create_list(4)
    linked_list.create_list(5)
    print("Original List:")
    linked_list.print_list()
    position = 3
    linked_list.deleteAtPosition(position)
    print(f"List after deleting node at position {position}:")
    linked_list.print_list()
    print()

if __name__ == "__main__":
    main()

        
        
