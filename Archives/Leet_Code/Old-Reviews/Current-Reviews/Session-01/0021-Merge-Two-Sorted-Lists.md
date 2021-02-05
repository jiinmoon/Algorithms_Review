21 Merge Two Sorted Lists
=========================

Merge two sorted linked lists and return it as sa new **sorted** list. The new
list should be made by splicing together the nodes of the first two lists.

---

We will simply iterate on the two lists, and compare their first nodes. Then,
we will append the smaller value unto the new list. This process is repeated
until we reach the end for either of the lists. The lists length may differ, in
which case we will append the remainder to the new list as well.

---

Go:

```go
func mergeTwoLists(l1, l2 *ListNode) *ListNode {
    var (
        dummyHead = &ListNode{}
        temp = &ListNode{}
        curr = dummyHead
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


