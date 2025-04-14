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

    void insert_node(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
    }

    void delete_at_end() {
        if (head == null) {
            System.out.println("List is empty. Nothing to delete.");
            return;
        }
        if (head.next == null) {
            head = null;
            return;
        }
        Node second_last_node = head;
        while (second_last_node.next.next != null) {
            second_last_node = second_last_node.next;
        }
        second_last_node.next = null;
    }

    void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }

}

public class delete_at_end {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.insert_node(10);
        list.insert_node(20);
        list.insert_node(30);
        list.insert_node(40);
        list.insert_node(50);
        System.out.println("Original List:");
        list.printList();
        list.delete_at_end();
        System.out.println("List after deleting at end:");
    }
}
