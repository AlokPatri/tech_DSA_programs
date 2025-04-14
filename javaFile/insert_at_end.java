class Node {
    int data;
    Node next;
    Node(int data) {
        this.data = data;
        this.next = null;

    }
}

class LinkedList {
    Node head;
    LinkedList() {
        this.head = null;
    }

    void insertAtEnd(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        Node lastNode = head;
        while (lastNode.next != null) {
            lastNode = lastNode.next;

        }
        lastNode.next = newNode;
    }

    void printList() {
        Node temp = head;
        while ( temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        } 
        System.out.println();
    }
}

public class insert_at_end {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.insertAtEnd(98);
        list.insertAtEnd(77);
        list.insertAtEnd(45);
        list.insertAtEnd(23);
        list.insertAtEnd(12);
        list.printList();
    }
}