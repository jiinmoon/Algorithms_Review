142 Linked List Cycle II
========================

Question:
---------

Given a linked list, return the node where the cyclebegins. If there is not
cycle, return `null`.

Solutions:
----------

A typical cycle detection algorithm (Floyd's) will work here. It will find the
overlapping node that marks the cycle. Now, from here, we will start a new
pointer from head to traverse forward with the pointer that has stopped at the
marked node until they are met. This will place them at the beginning of the
cycle.

Codes:
------

Go:

```go
func detectCycle(head *ListNode) *ListNode {
    var (
        fast = &ListNode{}
        slow = &ListNode{}
    )

```

---

**Source:**

LeetCode: [Question-Title](https://leetcode.com/problems/Question-Title)
