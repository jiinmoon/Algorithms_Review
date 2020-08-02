24 Swap Nodes in Pairs
======================

Question:
---------

Given a linked list, swap every two nodes and return its head.

Solutions:
----------

N/A.

Codes:
------

Go:

```go
func swapPairs(head *ListNode) *ListNode {
    var (
        dummyHead = &ListNode{}
        prev = dummyHead
    )
    for head != nil && head.Next != nil {
        temp := head.Next.Next
        prev.Next = head.Next
        head.Next.Next = head
        prev = head
        head = temp
    }
    prev.Next = head
    return dummyHead.Next
```

---

**Source:**

LeetCode:
[Swap-Nodes-in-Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
