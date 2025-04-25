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

    void insert(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    void reverseSubPart(Node head, int start, int end) {
        Node current = this.head, prev_m = null,
        mth = null, nth = null, after_n = null;
        for (int i = 1; current.next != null; i++, current = current.next) {
            if (i == start - 1) {
                prev_m = current;
            }
            if (i == start) {
                mth = current;
            }
            if (i == end) {
                nth = current;
                after_n = current.next;
                break;
            }
        }

    }
}