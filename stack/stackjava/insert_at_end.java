class Node {
    int data;
    Node next;
    Node(int data) {
        this.data = data;
    }   this.next = null;

}

class Stack {
    Node top;

    Stack() {
        this.top = null;
    }

    void push(int data) {
        Node newNode = new Node(data);
        if (top == null) {
            top = newNode;
            return;

        }
        Node temp = top;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = newNode;


    }

    void pop() {
        if (top == null) {
            System.out.println("Stack is empty");
            return;
        }
        temp = top;
        if (temp.next == null) {
            top = null;
            return;
        }
        while (temp.next.next != null) {
            temp = temp.next;
        }
        temp.next = null;
    }

    void display() {
        if (top == null) {
            System.out.println("Stack is empty");
            return;
        }
        Node temp = top;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }
}

public class insert_at_end {

    public static void main(String[] args) {
        Stack stack = new Stack();
        stack.push(10);
        stack.push(20);
        stack.push(30);
        stack.display(); // Output: 10 20 30
        stack.pop();
        stack.display(); // Output: 10 20
    }
}
