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

    void insertAtPosition(int position, int data) {
        Node newNode = new Node(data);
        if (position == 1) {
            newNode.next = head;
            head = newNode;
        }
        Node current = head;
        for(int i=1; i<position; i++) {
            if (current == null) {
                System.out.println("Position out of bounds");
                return;
            }
            current = current.next;
        }
        newNode.next = current.next;
        current.next = newNode;

    }
    void printList() {
        Node temp = head;
        while ( temp != null) {
            System.out.println(temp.data+ "-> ");
            temp = temp.next;
        }
    }


}

public class insert_at_position {

    public static void main(String[] args) {
        LinkedList link_list = new LinkedList();
        link_list.createList(10);
        link_list.createList(20);
        link_list.createList(30);
        System.out.println("befor inserting at position");
        link_list.printList();
        
        int position = 3;
        int data = 25;
        link_list.insertAtPosition(position, data);
        System.out.println("after inserting data at position");
        link_list.printList();
        
    }
}