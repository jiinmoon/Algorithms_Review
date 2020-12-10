# 876. Middle of the Linked List

Given a non-empty, singly linked list with head node head, return a middle node
of linked list.

If there are two middle nodes, return the second middle node.

---

We can perform this in a single iteration by having a first runner that is
moving at twice faster than the second runner. Bu doing so, second runner will
reach mid point when first runner has reached the end of the list.

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
class Solution876 {

    public ListNode middleNode(ListNode head) 
    {
        if (Objects.isNull(head) || Objects.isNull(head.next))
            return head;
        
        ListNode slow = head;
        
        for (;Objects.nonNull(head) && Objects.nonNull(head.next);
                slow = slow.next, head = head.next.next);
        
        return slow;
    }
}

```

