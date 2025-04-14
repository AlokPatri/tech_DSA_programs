class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def createList(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def mergetwoLinkedList(self, l1, l2):
        temp1 = self.l1.head
        temp2 = self.l2.head
        merged_list = LinkedList()
        while temp1:
            merged_list.createList(temp1.data)
            temp1 = temp1.next
        while temp2:
            merged_list.createList(temp2.data)
            temp2 = temp2.next
        return merged_list

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def main():
    l1 = LinkedList()
    l2 = LinkedList()
    l1.createList(1)
    l1.createList(3)
    l1.createList(5)
    l2.createList(2)
    l2.createList(4)
    l2.createList(6)
    print("List 1:")
    l1.printList()
    print("List 2:")
    l2.printList()
    merged_list = LinkedList()
    merged_list = merged_list.mergetwoLinkedList(l1, l2)
    print("print merged list")
    merged_list.printList()

if __name__=="__main__":
    main()