# 141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle
in it.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer. Internally, pos is
used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

---

#### (1) HashMap.

We iterate forward while record each node into a hashmap. If we see a duplicate
node, we have our cycle. O(n) in time and space.

#### (2) Floyd's Cycle Detection.

Use slow and fast pointers. Fast moves twice as fast as slow - if there is
a cycle, then fast eventually catches upto slow. O(n + k) in time complexity
where k is the lenth of the cycle.

---

Java; Floyd's Cycle Detection algorithm.

```java

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution141 {

    public boolean hasCycle(ListNode head) 
    {
        if (Objects.isNull(head) || Objects.isNull(head.next))
            return false;
        
        ListNode slow = head, fast = head.next;
        
        while (slow != fast)
        {
            if (Objects.isNull(fast) || Objects.isNull(fast.next))
                return false;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        return true;
    }
}
```
