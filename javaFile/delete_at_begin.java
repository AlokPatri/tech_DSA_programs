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
        Node lastNode = head;
        while (lastNode.next != null) {
            lastNode = lastNode.next;
        }
        lastNode.next = newNode;
    }

    void deleteAtBeginning() {
        Node temp = head;
        if (temp == null) {
            System.out.println("List is empty, nothing to delete.");
            return;
        }
        head = head.next;
        temp = null;
    }

    void printList() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }

}

public class delete_at_begin {

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.insert_node(98);
        list.insert_node(77);
        list.insert_node(45);
        list.insert_node(23);
        list.insert_node(12);
        System.out.println("Original List:");
        list.printList();
        
        list.deleteAtBeginning();
        System.out.println("After deleting at beginning:");
        list.printList();
    }
}
