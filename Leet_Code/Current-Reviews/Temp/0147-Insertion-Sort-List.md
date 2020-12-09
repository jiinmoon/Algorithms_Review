# 147. Insertion Sort List

Sort a linked list using insertion sort.

---

We iterate on the list; for each element or node, we have to place it or to
"insert" it in the sorted region of our sorted list. To do so, for every node
encountered, if it is less than the last node of our sorted region, we start
a search from the head to place it in its correct place.

O(n^2) in time complexity.

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
class Solution147 {

    public ListNode insertionSortList(ListNode head) 
    {
        ListNode dummy = new ListNode(Integer.MIN_VALUE);
        ListNode prev = dummy;
        dummy.next = head;
        
        while (Objects.nonNull(prev.next))
        {
            // current node to be sorted
            ListNode curr = prev.next;
            
            // no need to sort; move forward
            if (curr.val >= prev.val)
            {
                prev = prev.next;
                continue;
            }
            
            // sort
            // detach current node and move prev forward
            prev.next = prev.next.next;
            
            // start search from head
            ListNode runner = dummy;
            while (runner.next.val <= curr.val)
                runner = runner.next;
            
            curr.next = runner.next;
            runner.next = curr;
        }
        
        return dummy.next;
    }
}

```
