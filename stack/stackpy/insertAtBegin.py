class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if self.head is None:
            return
        temp = self.head
        self.head = self.head.next
        del temp
    
    def printStack(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

def main():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print("Stack after inserting elements at the beginning:")
    stack.printStack()
    
    stack.pop()
    
    print("Stack after deleting the top element:")
    stack.printStack()

if __name__ == "__main__":
    main()

