class Node {
    int data;
    Node next;
    Node (int data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    Node head;
    LinkedList() {
        this.head = null;
    }

    void insertAtBegin(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        newNode.next = head;
        head = newNode;
    }

    void printList() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.println("null");
    }
}
public class insert_at_begin {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.insertAtBegin(10);
        list.insertAtBegin(20);
        list.insertAtBegin(30);
        list.printList(); // Output: 30 -> 20 -> 10 -> null

    }
}
    