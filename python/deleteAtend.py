class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
    
    def delete_at_end(self):
        if self.head is None:
            print("list is empty:")
            return
        if self.head.next is None:
            self.head = None
            return
        second_node = self.head
        while second_node.next.next:
            second_node = second_node.next
        
        second_node.next = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None:")


def main():
    link_list=LinkedList()
    link_list.insert_node(1)
    link_list.insert_node(2)
    link_list.insert_node(3)
    print("Before deletion:")
    link_list.print_list()
    link_list.delete_at_end()
    print("After deletion:")
    link_list.print_list()


if __name__=="__main__":
    main()




