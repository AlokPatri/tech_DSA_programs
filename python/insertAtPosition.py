class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head= None
    
    def create_list(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insertATPosition(self, position, data):
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(1,position - 1):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next
    
        new_node.next = current.next
        current.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


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
    data = 10
    linked_list.insertATPosition(position, data)

    print(f"List after inserting {data} at position {position}:")
    linked_list.print_list()

if __name__ == "__main__":
    main()
        

        