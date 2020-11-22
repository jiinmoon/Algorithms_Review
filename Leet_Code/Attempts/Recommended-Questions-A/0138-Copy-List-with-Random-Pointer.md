# 138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.

---

We can efficiently create a deep copy of the given list using the hashmap - and
by doing so, we can avoid the problem of dealing the node that does not exist
yet which is pointed by the random variable. The copying process can complete
in a single iteration on the given array O(n) and it would also take O(n) space
complexity to copy all nodes.

---

Java:

```java

/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

import java.util.HashMap;

class Solution {
    public Node copyRandomList(Node head) {
        Map<Node, Node> m = new HashMap<>();
        Node curr = head;
        
        while (curr != null) {
            if (!m.containsKey(curr))
                m.put(curr, new Node(curr.val));
            if (curr.next != null) {
                if (!m.containsKey(curr.next))
                    m.put(curr.next, new Node(curr.next.val));
                m.get(curr).next = m.get(curr.next);
            }
            if (curr.random != null) {
                if (!m.containsKey(curr.random)
                    m.put(curr.random, new Node(curr.random.val));
                m.get(curr).random = m.get(curr.random);
            }
            curr = curr.next;
        }

        return m.get(head);
    }
}

```

Python:

```python

class Solution:
    def copyList(self, head):
        d = dict()
        curr = head
        while curr:
            if curr not in d:
                d[curr] = ListNode(curr.val, None, None)
            if curr.next:
                if curr.next not in d:
                    d[curr.next] = ListNode(curr.next.val, None, None)
                d[curr].next = d[curr.next]
            if curr.random:
                if curr.random not in d:
                    d[curr.random] = ListNode(curr.random.val, None, None)
                d[curr].random = d[curr.random]
            curr = curr.next

        return d[head]
```
