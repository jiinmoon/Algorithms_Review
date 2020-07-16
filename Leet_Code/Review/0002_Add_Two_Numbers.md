[2] Add Two Numbers
===================

You are given two **non-empty** linked lists representing two non-negative
integers. The digits are stored in **reverse order** and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

**Example**:

```
Input: (2, 4, 3) + (5, 6, 4)
Output: (7, 0, 8)
```

Solution
--------

We would simply iterate on the lists and sum them together. If we want to be
more clear and maintain a good code base, then we would think about making it
into several components that are specializes into a single task. Here we would
need to convert list to integer, add them together, and convert back into the
list format.

**Python3**

```python
class Solution:
    def list_to_int(self, head):
        result = 0
        i = 0
        while head:
            result += head.val * 10 ** i
            i += 1
            head = head.next
        return result

    def int_to_list(self, num):
        dummyHead = curr = ListNode(None)
        while num:
            curr.next = ListNode(num % 10)
            num //= 10
            curr = curr.next
        return dummyHead.next

    def add_two_numbers(self, li1, li2):
        if not li1 or not li2:
            return li1 or li2
        result = self.list_to_int(li1) + self.list_to_int(li2)
        return self.int_to_list(result)
```

**Go**

The problem is that the number can overflow with other languages if we are
trying to fit the converted number into a single int type. In this case, the
safe approach would be to avoid this problem and compute as we iterate on list,
or use `BigInteger` type of library.

```go
func add_two_numbers(l1 *ListNode, l2 *ListNode) *ListNode {
    dummyHead := &ListNode{}
    curr := dummyHead

    sum, carry := 0, 0
    for carry != 0 || l1 != nil || l2 != nil {
        curr.Next = &ListNode{}
        curr = curr.Next
        sum = carry
        if l1 != nil {
            sum += l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            sum += l2.Val
            l2 = l2.Next
        }
        curr.Val = sum % 10
        carry = sum / 10
    }
    return dummyHead.Next
}
```


---

LeetCode: [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
