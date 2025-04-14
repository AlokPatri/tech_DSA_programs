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
        return self.head
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

def main():
    linked_list = LinkedList()

    linked_list.insert_at_begin(10)
    linked_list.insert_at_begin(20)
    linked_list.insert_at_begin(30)
    linked_list.insert_at_begin(40)
    linked_list.insert_at_begin(50)
    linked_list.print_list()

if __name__ == "__main__":
    main()
    

