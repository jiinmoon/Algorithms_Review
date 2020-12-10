# 143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be
changed.

---

We reverse the second half of the linked list, and weave them together into
a new singly linked list.

O(n) in time complexity.

---

Java:

```java

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    
    public void reorderList(ListNode head) 
    {
        if (Objects.isNull(head) || Objects.isNull(head.next))
            return;
        
        ListNode prev, slow, fast, secondHead, dummyHead;
        slow = fast = head;
        prev = null;
        
        for (; Objects.nonNull(fast) && Objects.nonNull(fast.next);
                prev = slow, slow = slow.next, fast = fast.next.next);
        
        prev.next = null;
        secondHead = null;
        
        while (Objects.nonNull(slow))
        {
            ListNode temp = slow.next;
            slow.next = secondHead;
            secondHead = slow;
            slow = temp;
        }
        
        boolean flip = true;
        dummyHead = prev = new ListNode(0);
        
        while (Objects.nonNull(secondHead) && Objects.nonNull(head))
        {
            if (flip) {
                prev.next = head;
                head = head.next;
            } else {
                prev.next = secondHead;
                secondHead = secondHead.next;
            }
            flip = !flip;
            prev = prev.next;
        }
        
        prev.next = (Objects.nonNull(head)) ? head : secondHead;
        
        head = dummyHead.next;
    }
}
```
