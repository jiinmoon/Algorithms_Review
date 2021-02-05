# 206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you
implement both?

---

#### (1) Iterative.

We move forward on current node while fixing the current node's next to
previous. O(n) in time complexity and O(1) in space complexity.

#### (2) Recursive.

We first move all the way down to the bottom of our recursive call. Bottom-up
we fix the current node's next pointers. Due to having to save stack calls,
O(n) in space complexity and O(n) in time complexity.

---

Python: iterative.

```python

class Solution206:

    def reverseList(self, head):

        if not (head and not head.next):
            return head

        prev = None

        while head:
            temp = head.next
            head.next = temp
            temp = head
            head = temp

        return prev
```

Python: recursive.

```python

class Solution206:

    def reverseList(self, head):

        if not (head and not head.next):
            return head

        prev = self.reverseList(head)
        
        # next node points back
        head.next.next = head
        head.next = None

        return prev
```

