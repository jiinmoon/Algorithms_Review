23 Merge k Sorted Lists
=======================

Question:
---------

Merge k sorted linked lists and return it as a one sorted list.

Solutions:
---------

The simplest solution would be a naive iteration of continuously polling from
the list of lists, comparing their first element and build our new sorted list.

Another similar brute force solution is to collect all the values, sort the
values and create a new linked list from it. This will be O(n * log(n)).

However, we can design a better algorithm by repeatedly calling merge two
sorted lists until we have single list left over. If we can pair-up the lists,
then it can complete the task in log(k) depth where k is the number of lists to
merge. Thus, the time complexity reduces to O(n * log(k)) from O(n * k).

Codes:
------

Python3:

```python
class Solution:
    def mergeTwoSortedLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if not l1 and not l2:
            return None
        dummyHead = curr = ListNode(None)
        while l1 or l2:
            if l1.val < l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp = l2
                l2 = l2.next
            curr.next = temp
            curr = curr.next
        curr.next = l1 or l2
        return dummyHead.next

    def mergeKSortedLists(self, lists):
        if not lists:
            return None
        while lists:
            temp = []
            while lists:
                l1 = lists.pop()
                l2 = lists.pop() if lists else None
                temp.append(self.mergeTwoSortedLists(l1, l2))
            lists = temp
        return lists[0]
```

Go:

```go
func mergeTwoLists(l1, l2 *ListNode) *ListNode {
    if l1 == nil {
        return l2
    }
    if l2 == nil {
        return l1
    }

    if l1.val < l2.val {
        l1.Next = mergeTwoLists(l1.Next, l2)
        return l1
    } else {
        l2.Next = mergeTwoLists(l1, l2.Next)
        return l2
    }

}

func mergeKSortedLists(lists []*ListNode) *ListNode {
    if lists == nil {
        return nil
    }
    for ;len(lists) > 1; lists[2:] {
        l1, l2 := lists[0], lists[1]
        lists.append(lists, mergeTwoLists(l1, l2))
    }
    return lists[0]
}
```

---

**Source:**

LeetCode:
[Merge-k-Sorted-Lists](https://leetcode.com/problems/merge-k-sorted-lists/))
