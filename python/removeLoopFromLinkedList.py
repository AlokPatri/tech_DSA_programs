class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def creatte_linkedList(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node

    def remove_loop(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        
        if slow != fast:
            return

        start = self.head
        if slow == start:
            while fast.next != self.head:
                fast = fast.next 
        
        else:
            while start.next != slow.next:
                start = start.next
                slow = slow.next

        slow.next = None
        print("Loop removed from the linked list")
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def main():
    llist = LinkedList()
    llist.creatte_linkedList(1)
    llist.creatte_linkedList(2)
    llist.creatte_linkedList(3)
    llist.creatte_linkedList(4)
    llist.creatte_linkedList(5)

    # Creating a loop for testing
    llist.head.next.next.next.next.next = llist.head.next

    print("Linked List before removing loop:")
    llist.print_list()

    llist.remove_loop()

    print("Linked List after removing loop:")
    llist.print_list()

if __name__ == "__main__":
    main()
    