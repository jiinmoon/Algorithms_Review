# 92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

---

First, iterate upto m; then start the reversal process. Make sure to save the
previous pointer to the last node before reversal begins to reattach the
reversed list back to the original list.

O(n) in time complexity and O(1) in space complexity.

---

Java:

```java

class Solution92 {

    public ListNode reverseBetween(ListNode head, int m, int n)
    {
        ListNode dummy, prev;
        dummy = prev = ListNode(0);
        dummy.next = head;
        
        // move prev only to the previous to the start of reversed list
        while (m-- > 1)
            prev = prev.next;
        
        // reverse
        ListNode newHead = null, newTail = prev.next, temp;
        n -= m
        while (n-- >= 0)
        {
            temp = newTail.next;
            newTail.next = newHead;
            newHead = newTail;
            newTail = temp;
        }

        // join reversed list back to original
        prev.next.next = newTail;
        prev.next = newHead;

        return dummy.next;
    }
}

```

