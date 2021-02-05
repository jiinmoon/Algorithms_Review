# 24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be
changed.

---

Java:

```java

class Solution24 {

    public ListNode swapPairs(ListNode head)
    {
        ListNode dummy, prev;
        dummy = prev = new ListNode(0);

        while (Objects.nonNull(head) && Objects.nonNull(head.next))
        {
            // save pointer to next pair
            ListNode temp = head.next.next;

            // let end of our new list point at start of our new head
            prev.next = head.next;
            // let second part of pair loop back to first part
            head.next.next = head;
            // prev moves to start of new pair
            prev = head;
            // head moves forward to new pair
            head = temp;
        }

        return dummy.next;
    }
}

```
