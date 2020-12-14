# 146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used
(LRU) cache.

Implement the LRUCache class:

```
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

int get(int key) Return the value of the key if the key exists, otherwise
return -1.

void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the number of keys exceeds
the capacity from this operation, evict the least recently used key.
```

Follow up:

Could you do get and put in O(1) time complexity?

---

(1) Queue and Hashmap.

To keep track of any kind of ordering (i.e. LRU), we require queue data
structure to choose the item to evict. Problem here is the update. To update
a key, we have to linearly scan the queue to find the element, and then reorder
the elements in the queue. This would be O(n) in time complexity for `put()`
operation.

(2) Hashmap with doubly linked list.

Some data structures such as `OrderedDict` in Python or `LinkedHashMap` in Java
is able to maintain the order of the elements as well as update its elements in
O(1) via implementing the hashmap with doubly linked-list. Hence, we can
achieve O(1) time complexity for both `put` and `get`.

It works by being able to update the given node in constant time with doubly
linked list. So, we maintain a hashmap of these key to node pairs. Most
recently used elements will always be placed at the head, and items to evict
will be at the end of list or at tail.

---

Java: HashMap + Doubly Linked List approach.

```java

class Solution146 {

    static class ListNode {
        private int key, value;
        private ListNode next, prev;

        public ListNode()
        {
            this(0, 0);
            this.next = null;
            this.prev = null;
        }

        public ListNode(int key, int value)
        {
            this.key = key;
            this.value = value;
        }
    }

    private final int CACHE_CAPACITY;
    private int cache_size;
    private Map<Integer, ListNode> map;
    private ListNode head, tail;

    public Solution146(int capacity)
    {
        this.CACHE_CAPACITY = capacity;
        this.cache_size = 0;
        this.map = new HashMap<>();
        this.head = new ListNode();
        this.tail = new ListNode();
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    public int get(int key)
    {
        if (!this.map.containsKey(key)
            return -1;
        
        // update node to front of list
        ListNode node = this.map.get(key); 
        deleteNode(node);
        addToFront(node);
        return node.value;
    }

    public void put(int key, int value)
    {
        if (this.map.containsKey(key)) {

            // update node to front of list
            ListNode node = this.map.get(key);
            node.value = value;
            deleteNode(node);
            addToFront(node);

        } else {

            if (this.CACHE_CAPACITY <= this.cache_size) 
                this.map.remove(removeFromBack().key);
            
            // new nodes are placed in front of list
            ListNode newNode = new ListNode(key, value);
            this.map.put(key, newNode);
            addToFront(newNode);
            this.cache_size++;
        }
    }

    private void deleteNode(ListNode node)
    {
        if (node == null)
            return;

        // delete node in-place;
        // previous node skips over this node
        ListNode prev = node.prev;
        ListNode next = node.next;
        prev.next = next;
        next.prev = prev;
    }
    
    private void addToFront(ListNode node)
    {
        // add node to head
        node.prev = this.head;
        node.next = this.head.next;
        this.head.next.prev = node;
        this.head.next = node;
    }

    private void removeFromBack()
    {
        ListNode node = this.tail.prev;
        deleteNode(node);
        return node;
    }
}

```

Python: OrderedDict approach.

```python

from collections import OrderedDict

class Solution146:

    def __init__(self, capacity):
        self.capacity = capacity
        self.d = OrderedDict()

    def get(self, key):
        if key not in self.d:
            return -1
        # update recently used item
        val = self.d.pop(key)
        self.d[key] = val
        return val
    
    def put(self, key, val):
        if key in self.d:
            # key is in, update its order first then update its value
            self.get(key)
        elif self.capacity == len(self.d):
            # first item is least recently used item
            self.d.pop(next(iter(self.d)))
        self.d[key] = val

```
