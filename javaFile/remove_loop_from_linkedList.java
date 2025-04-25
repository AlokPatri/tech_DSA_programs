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

    void append(int data) {
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

    void createLoop(int position) {
        Node temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = head.next.next;
    }

    void removeLoop() {
        Node temp1 = head;
        Node temp2 = head;

        // Detect loop using Floyd's cycle detection algorithm
        while ((temp2 != null) || (temp2.next != null)) {
            temp1 = temp1.next;
            temp2 = temp2.next.next;

            // If loop exists, break
            if (temp1 == temp2) {
                break;
            }
        }
        // If no loop exists, return
        if (temp1 == temp2) {
            temp1 = head;
            while (temp1 != temp2) {
                temp1 = temp1.next;
                temp2 = temp2.next;
            }
            // last node
            while (temp1.next != temp2) {
                temp1 = temp1.next;

            }
            temp2.next = null; // remove loop

        }
    }

    void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }
}

public class remove_loop_from_linkedList {

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.append(1);
        list.append(2);
        list.append(3);
        list.append(4);
        list.append(5);

        list.createLoop(2); // Create a loop for testing
        list.removeLoop(); // Remove the loop
        list.printList(); // Print the list after removing the loop

        
    }
}
