# Reverse Linked List II

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:

Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.


Note:

Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list. Note 2:
Usually the version often seen in the interviews is reversing the whole linked
list which is obviously an easier version of this question. 

---

We first traverse previous to the m-th node, this pointer needs to be saved in
order for us to reattach to the new head of the reversed segment. Starting from
this place, we reverse upto (n - m) times.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def reverseBetween(self, A, B, C):

        dummy = prev = ListNode(None)
        dummy.next = A
        # we need to perform reversal for C - B amonut of times
        C -= B
        
        # move previous to B-th node
        for _ in range(B - 1):
            prev = prev.next
        
        # newHead and newTail of the reversed segment
        newHead, newTail = None, prev.next

        # reverse
        for _ in range(C + 1):
            temp = newTail.next
            newTail.next = newHead
            newHead = newTail
            newTail = temp
        
        # reattach reversed segment
        prev.next.next = newTail
        prev.next = newHead

        return dummy.next
```

