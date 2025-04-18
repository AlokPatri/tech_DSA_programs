class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove_duplicates(self):
        #without using extra space
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def main():
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(2)
    ll.push(3)
    
  

    print("Original list:")
    ll.print_list()

    ll.remove_duplicates()

    print("List after removing duplicates:")
    ll.print_list()

if __name__ == "__main__":
    main()