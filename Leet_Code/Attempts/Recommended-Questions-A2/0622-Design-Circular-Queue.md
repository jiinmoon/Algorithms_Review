# 622. Design Circular Queue

Design your implementation of the circular queue. The circular queue is
a linear data structure in which the operations are performed based on FIFO
(First In First Out) principle and the last position is connected back to the
first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces
in front of the queue. In a normal queue, once the queue becomes full, we
cannot insert the next element even if there is a space in front of the queue.
But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

```
MyCircularQueue(k): Constructor, set the size of the queue to be k.

Front: Get the front item from the queue. If the queue is empty, return -1.

Rear: Get the last item from the queue. If the queue is empty, return -1.

enQueue(value): Insert an element into the circular queue. Return true if the
operation is successful.

deQueue(): Delete an element from the circular queue. Return true if the
operation is successful.

isEmpty(): Checks whether the circular queue is empty or not.

isFull(): Checks whether the circular queue is full or not.
```

---

There are two general approach to implement a circular queue that supports
specified operations - with either a linked list or circular array. In either
cases, we keep track of head and tail so that we can identify front and rear
items as well as remove them as quickly as possible.

With circular array approach, we have an array of items. And two pointer
indicies are maintained for head and tail. Head points at the first item in the
queue, and tail points at the next insertion point in the queue.

Hence, enqueue operation is simply inserting the value pointed by the tail
pointer. And tail pointer is incremented + 1 but with modulo size of the queue
to wrap around the size.

dequeue operation would be inverse: we advance the head pointer forward.

front and rear would simply be retrieveing the items pointed by the head and
tail. BUt for tail, as it is pointing at the next insertion index, it should be
decremented first to retrieve the value.

To determine whether this queue is empty or not, we check whether two head and
tail pointers have met. If it is empty, the tail pointer index should be empty
and available to accept a new item; otherwise, it is full.

Linked List is also a viable option but would in general take more space due to
having to maintain more variables; while it offers flexibility to grow and to
shrink the list in O(1), since the size here is fixed, we do not have to opt
for Linked List structure here.

---

Java: Circular Array approach;

```java

class Solution622 {
    
    private int size, head, tail;
    private Integer[] queue;

    public Solution622(int k)
    {
        this.size = k;
        this.head = 0;
        this.tail = 0;
        this.queue = new Integer[k];
    }

    public boolean enQueue(int value)
    {
        if (this.isFull()) return false;
        this.queue[this.tail] = value;
        this.tail = (this.tail + 1) % this.size;
        return true;
    }

    public boolean deQueue()
    {
        if (this.isEmpty()) return false;
        this.queue[this.head] = null;
        this.head = (this.head + 1) % this.size;
        return true;
    }

    public int front()
    { return (this.isEmpty()) ? -1 : this.queue[Math.floorMod(this.head, this.size)]; }

    public int rear()
    { return (this.isEmpty()) ? -1 : this.queue(Math.floorMod(this.tail-1, this.size()]; }

    public boolean isFull()
    { return this.head == this.tail && this.queue[this.tail] != null; }

    public boolean isEmpty()
    { return !this.isFull() }
}

```

Java: Linked List approach;

```java

class Solution622 {

    static class ListNode {
        private int val;
        private ListNode next;

        public ListNode(int val) {
            this.val = val;
        }
    }

    private int size, capacity;
    private ListNode head, tail;

    public Solution622(int k) { this.capacity == k; }
    
    public boolean enQueue(int val)
    {
        if (this.isFull())
            return false;

        ListNode newNode = new ListNode(val);
        if (this.size == 0) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.size++;
        return true;
    }

    public boolean deQueue(int val)
    {
        if (this.isEmpty())
            return false;
        this.size--;
        if (this.size == 0) {
            this.head = null;
            this.tail = null;
        } else {
            this.head = this.head.next;
        }
        return true;
    }

    public int front() { return (this.isEmpty()) ? -1 : this.head.val; }
    public int rear() { return (this.isEmpty()) ? -1 : this.tail.val; }
    public boolean isEmpty() { return this.size == 0; }
    public boolean isFull() { return this.size == this.capacity; }
}

```
