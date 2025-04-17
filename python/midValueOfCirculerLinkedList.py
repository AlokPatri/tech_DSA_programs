class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleCirculerLinkedlist:
    def __init__(self):
        self.head = None

    def createLinkedList(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = self.head

    def midValueOfCirculerLinkedList(self):
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is not None:
            while (fast_ptr.next != self.head and fast_ptr.next.next != self.head):
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next

        return slow_ptr.data
    def printList(self):
        current_node = self.head
        if self.head is not None:
            while True:
                print(current_node.data, end=" ")
                current_node = current_node.next
                if current_node == self.head:
                    break
        print()

def main():
    cll = SingleCirculerLinkedlist()
    cll.createLinkedList(10)
    cll.createLinkedList(20)
    cll.createLinkedList(30)
    cll.createLinkedList(40)
    cll.createLinkedList(50)
    print("Single Circuler Linked List:")
    cll.printList()
    mid_value = cll.midValueOfCirculerLinkedList()
    print("Mid value of Circuler Linked List:", mid_value)

if __name__ == "__main__":
    main()