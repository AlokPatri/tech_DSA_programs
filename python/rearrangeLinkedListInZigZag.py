class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_linkedList(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node

    def rearrange_zigzag(self):
        current = self.head
        flag = True  # True for '<', False for '>'

        while current and current.next:
            if flag:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
            else:
                if current.data < current.next.data:
                    current.data, current.next.data = current.next.data, current.data
            
            flag = not flag
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def main():
    llist = LinkedList()
    llist.create_linkedList(1)
    llist.create_linkedList(3)
    llist.create_linkedList(2)
    llist.create_linkedList(7)
    llist.create_linkedList(5)
    llist.create_linkedList(4)

    print("Original linked list:")
    llist.print_list()

    llist.rearrange_zigzag()

    print("Zigzag rearranged linked list:")
    llist.print_list()

if __name__ == "__main__":
    main()

