2. Add Two Numbers
==================

Question:
---------

Given two **non-empty** linked list represneting integers, add the two together
and return in linked list format.

Solutions:
----------

Simply, we will iterate on and add the values together. We create a new list
node for current sum % 10, and then move over the carry to next iteration.

Codes:
------

Go:

```go
func addTwoNumbers(l1, l2 *ListNode) *ListNode {
    var (
        dummyHead = &ListNode{}
        currNode = dummyHead
        currSum = 0
    )

    for l1 != nil || l2 != nil || currSum != 0 {
        if l1 != nil {
            currSum += l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            currSum += l2.Val
            l2 = l2.Next
        }
        currNode.Next = &ListNode{ Val: currSum % 10 }
        currSum /= 10
        currNode = currNode.Next
    }
    return dummyHead.Next
}
```

---

**Source:**

LeetCode: [Add-Two-Numbers](https://leetcode.com/problems/add-two-numbers/)
