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

    void reverseSubPart(int start, int end) {
        if (head == null || start >= end) {
            return;
        }

        Node dummy = new Node(0);
        dummy.next = head;
        Node prev = dummy;

        for (int i = 0; i < start - 1; i++) {
            if (prev == null) {
                return;
            }
            prev = prev.next;
        }

        Node current = prev.next;
        Node tail = current;

        for (int i = 0; i < end - start; i++) {
            if (tail == null) {
                return;
            }
            tail = tail.next;
        }

        Node next = tail.next;
        tail.next = null;

        prev.next = reverse(current);
        current.next = next;
    }
}