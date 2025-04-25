class Node:
    def __init__(self, data):
        self.data = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def reverse_sub_part(self, start, end):
        if start == end:
            return

        prev = None
        current = self.head

        # Move to the start position
        for _ in range(start - 1):
            prev = current
            current = current.next

        last_node_of_first_part = prev
        last_node_of_sub_list = current

        # Reverse the sub-list
        next_node = None
        for _ in range(end - start + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        if last_node_of_first_part:
            last_node_of_first_part.next = prev
        else:
            self.head = prev

        last_node_of_sub_list.next = current

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def main():
    llist = LinkedList()
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)

    print("Original Linked List:")
    llist.print_list()

    start = 2
    end = 4
    llist.reverse_sub_part(start, end)

    print(f"Reversed sub-part from {start} to {end}:")
    llist.print_list()

if __name__ == "__main__":
    main()
    