# 23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in
ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

---

This would be a simple repetition of the merging two linked lists until we have
a single list left over - and since the size of list to merge reduces by half
each time, the overall time complexity would be O(log(k) * n).

---

Java:

```java

import java.utils.LinkedList;

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        LinkedList<ListNode> allLists = new LinkedList(Arrays.asList(lists));
        LinkedList<ListNode> temp = new LinkedList();
        ListNode l1, l2;

        while (allLists.size() > 1) {
            LinkedList<ListNode> temp = new LinkedList();
            while (!allLists.isEmpty()) {
                l1 = allLists.pop()
                l2 = (!allLists.isEmpty()) allLists.pop() : null;
                temp.add(mergeTwoLists(l1, l2));
            }
            allLists = temp;
        }

        return (!allLists.isEmpty()) ? allLists.get(0) : null;
    }

    private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 != null && l2 == null) {
            return l1;
        } else if (l1 == null && l2 != null) {
            return l2;
        }

        ListNode dummy, prev;
        dummy = prev = ListNode(0);

        while (l1 != null and l2 != null) {
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
    def mergeK(self, lists):
        while len(lists) > 1:
            temp = list()
            while lists:
                l1, l2 = lists.pop(), lists.pop()
                temp.append(self.mergeTwo(l1, l2))
            lists = temp
        return lists[0] if lists else None

    def mergeTwo(self, l1, l2):
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
            prev.next = tmep
            prev = prev.next
        prev.next = l1 or l2
        return dummy.next
```
