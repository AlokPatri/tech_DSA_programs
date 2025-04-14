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

    void createList(int data){
        Node newNode = new Node( data);
        if (head == null){
            head = newNode;
            return;
        }
        Node current = head;
        while  (current.next != null) {
            current = current.next;
        }
        current.next = newNode;

    }

    void deleteAtPosition(int position) {
        if (head == null) {
            System.out.println("List is empty");
            return;
        }
        if (position == 1) {
            head = head.next;
            return;
        }
        Node current = head;
        for (int i = 1; i < position - 1; i++) {
            if (current == null || current.next == null) {
                System.out.println("Position out of bounds");
                return;
            }
            current = current.next;
        }
        if (current.next == null) {
            System.out.println("Position out of bounds");
            return;
        }
        current.next = current.next.next;
    }
    void printList() {
        Node temp = head;
        while ( temp != null) {
            System.out.println(temp.data+ "-> ");
            temp = temp.next;
        }
    }

public class delete_at_position {

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.createList(1);
        list.createList(2);
        list.createList(3);
        list.createList(4);
        list.createList(5);
        System.out.println("Original List:");
        list.printList();
        
        int positionToDelete = 3;
        list.deleteAtPosition(positionToDelete);
        
        System.out.println("List after deleting at position " + positionToDelete + ":");
        list.printList();
    }
}