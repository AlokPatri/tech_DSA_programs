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
        
    def reverseLinkedList(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current

            current = next_node
        self.head = prev

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        
def main():
    list = LinkedList()
    list.createList(10)
    list.createList(20)
    list.createList(30)
    list.createList(40)
    print("list before reversing")
    list.printList()

    print("printing reverse liked list")
    list.reverseLinkedList()
    list.printList()

if __name__=="__main__":
    main()
    


    