# 21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list. The new list
should be made by splicing together the nodes of the first two lists.

---

Given two sorted linked lists, we start from the either end of the list and
append the smaller node to the new list to be returned. We take a note of the
irregular length of the two lists - thus, append the whichever list that is
left over.

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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 != null && l2 == null) {
            return l1;
        } else if (l1 == null && l2 != null) {
            return l2;
        }

        ListNode dummy, prev;
        dummy = prev = ListNode();

        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                prev.next = l1;
                l1 = l1.next;
            } else {
                prev.next = l2;
                l2 = l2.next;
            }
            prev = prev.next;
        }

        prev.next = (l1 != null) ? l1 : l2;

        return dummy.next;
    }
}

 ```

Python:

```python

class Solution:
    def mergeTwoLinkedLists(self, l1, l2):
        if not (l1 or l2):
            return l1 or l2

        dummy = prev = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp = l2
                l2 = l2.next
            prev.next = temp
            prev = prev.next
        prev.next = l1 or l2

        return dummy.next
```
