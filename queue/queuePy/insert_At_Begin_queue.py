class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = Node
    
    def enQueue(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNonde
            return
        
        newNode.next = self.head
        self.head = newNode
        return
    
    def deQueue(self):
        if self.head is None:
            return
        
        temp = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        del temp
        prev.next = None

        def printQueue(self):
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

def main():
    queue = Queue()
    queue.enQueue(10)
    queue.enQueue(20)
    queue.enQueue(30)

    print("Queue after inserting elements at the beginning:")
    queue.printQueue()

    queue.deQueue()

    print("Queue after deleting the last element:")
    queue.printQueue()

if __name__ == "__main__":
    main()

    

    
