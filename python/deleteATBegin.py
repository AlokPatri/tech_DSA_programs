# 1.create linked list and delete a node at the beginning of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delete_at_begin(self):
        temp = self.head
        if self.head is None:
            print("list is empty:")
            return
        self.head = self.head.next
        temp = None
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None:")


def main():
    ll = LinkedList()
    ll.insert_at_begin(1)
    ll.insert_at_begin(2)
    ll.insert_at_begin(3)
    print("Before deletion:")
    ll.print_list()
    
    ll.delete_at_begin()
    print("After deletion:")
    ll.print_list()

if __name__ == "__main__":
    main()
    