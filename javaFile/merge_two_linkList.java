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

    void create_list(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } 
        Node last_node = head;
        while (last_node.next != null) {
            last_node = last_node.next;
        }
        last_node.next = newNode;
    }

    void merge_two_linked_list (LinkedList list1, LinkedList list2) {
        Node current1 = list1.head;
        Node current2 = list2.head;
        LinkedList mergedList = new LinkedList();

        while (current1 != null && current2 != null) {
            if (current1.data < current2.data) {
                mergedList.create_list(current1.data);
                current1 = current1.next;
            } else {
                mergedList.create_list(current2.data);
                current2 = current2.next;
            }
        }

        while (current1 != null) {
            mergedList.create_list(current1.data);
            current1 = current1.next;
        }

        while (current2 != null) {
            mergedList.create_list(current2.data);
            current2 = current2.next;
        }

        mergedList.printList();

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

public class  merge_two_linkList {
    public static void main(String[] args) {
        LinkedList list1 = new LinkedList();
        list1.create_list(1);
        list1.create_list(3);
        list1.create_list(5);

        LinkedList list2 = new LinkedList();
        list2.create_list(2);
        list2.create_list(4);
        list2.create_list(6);

        LinkedList mergedList = new LinkedList();
        mergedList.merge_two_linked_list(list1, list2);
    }
}