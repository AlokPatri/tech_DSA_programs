class Node {
    int data;
    Node next;
    Node (int data) {
        this.data = data;
        this.next = null;
    }
}

class SingleCircularLinkedList {
    Node head = null;

    SingleCircularLinkedList() {
        this.head = null;

    }

    void createLinkedList(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            head.next = head; // Point to itself to make it circular
        } else {
            Node current = head;
            while (current.next != head) {
                current = current.next;
            }
            current.next = newNode;
            newNode.next = head; // Point the new node to the head to maintain circularity
        }
    }

    void midValue() {
        if (head == null) {
            System.out.println("List is empty. No mid value.");
            return;
        }
        Node slow = head;
        Node fast = head;
        while (fast.next != head && fast.next.next != head) {
            slow = slow.next;
            fast = fast.next.next;
        }
        System.out.println("Mid value: " + slow.data);
        
    }

    void printList() {
        if (head == null) {
            System.out.println("List is empty.");
            return;
        }
        Node current = head;
        do {
            System.out.print(current.data + " -> ");
            current = current.next;
        } while (current != head);
        System.out.println("(head)");
    }
}

public class find_midValue_in_single_circuler_linked_list {
    public static void main(String[] args) {
        SingleCircularLinkedList list = new SingleCircularLinkedList();
        list.createLinkedList(10);
        list.createLinkedList(20);
        list.createLinkedList(30);
        list.createLinkedList(40);
        list.createLinkedList(50);
        list.printList();
        System.err.println("Mid value in the list: ");

        list.midValue();
    }
}