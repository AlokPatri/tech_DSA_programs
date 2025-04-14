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

    def rotateLinkedList(self, k):
        if  self.head == None or self.head.next == None or k <= 0:
            return
        
        current = self.head
        length = 1
        while current.next != None:
            current = current.next
            length+=1

        current.next = self.head
        k = k % length
        stepsToNewHead = length - k
        current = self.head
        for i in range(1, stepsToNewHead):
            current = current.next

        self.head = current.next
        current.next = None
    
    def printList(sefl):
        temp = sefl.head
        while temp:
            print(temp.data, end="-> ")
            temp = temp.next

        print(None)

def main():
    list = LinkedList()
    list.createList(10)
    list.createList(20)
    list.createList(30)
    list.createList(40)
    list.createList(50)
    print("list before rotating")
    list.printList()
    k = 2
    list.rotateLinkedList(2)
    print("printing rotate list")
    list.printList()

if __name__=="__main__":
    main()

