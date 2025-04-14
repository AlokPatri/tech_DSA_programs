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

    void create_list(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        Node last_node = newNode;
        while (last_node != null) {
            last_node = last_node.next;
            
        }
        last_node.next = newNode;
        
    }

    void reverseLikedList() {
        Node prev = null;
        Node current = head;
        while ( current != null) {
            Node nextNode = current.next;
            current.next = prev;
            prev = current;
            
            current = nextNode;
            
        }
        head = prev;

    }
    void printList() {
        Node temp = head;
        while ( temp != null) {
            System.out.println(temp.data+"->");
            temp = temp.next;
            
        }
        System.out.println("none");
    }
}

public class reverse_linked_list {

     public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.create_list(10);
        list.create_list(20);
        list.create_list(30);
        list.create_list(40);
        System.out.println("printing list befor reverse");
        
        list.printList();
        list.reverseLikedList();
        System.out.println("printing list after reversing");
        list.printList();

     }
}