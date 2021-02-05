21 Merge Two Sorted Lists
=========================

Question:
---------

Merge two sorted linked lists and return it as a new **sorted** list. The new
list should splice of given lists.

Solutions:
----------

We will create a new head where we will attach the nodes from sorted linked
lists in order.

Codes:
------

Go:

```go
fun mergeTwoLists(l1, l2 *ListNode) *ListNode {
    var (
        dummyHead = &ListNode{}
        curr = dummyHead
        temp = &ListNode{}
    )
    for l1 != nil && l2 != nil {
        if l1.Val < l2.Val {
            temp = l1
            l1 = l1.Next
        } else {
            temp = l2
            l2 = l2.Next
        }
        curr.Next = temp
        curr = curr.Next
    }
    if l1 != nil {
        curr.Next = l1
    } else {
        curr.Next = l2
    }
    return dummyHead.Next
}
```

---

**Source:**

LeetCode: [Merge-Two-Sorted-Lists](https://leetcode.com/problems/merge-two-sorted-lists)
