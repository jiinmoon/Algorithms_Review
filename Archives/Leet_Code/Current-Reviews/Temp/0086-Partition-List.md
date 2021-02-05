# 86. Partition List

Given a linked list and a value x, partition it such that all nodes less than
x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two
partitions.

---

Create two lists where one stores nodes less than x and other greater than x.
In the end, concatenate two lists together.

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
class Solution86 {

    public ListNode partition(ListNode head, int x) 
    {
        ListNode dummyLess, dummyGreat, less, great;
        dummyLess = less = new ListNode(0);
        dummyGreat = great = new ListNode(0);
        
        while (Objects.nonNull(head))
        {
            if (head.val < x) {
                less.next = head;
                less = head;
            } else {
                great.next = head;
                great = head;
            }
            head = head.next;
        }
        
        less.next = dummyGreat.next;
        great.next = null;
        
        return dummyLess.next;
    }
}

```
