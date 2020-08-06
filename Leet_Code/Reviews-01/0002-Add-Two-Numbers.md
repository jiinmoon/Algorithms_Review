1 Two Sum
=========

Given two **non-empty** linked lists representing two non-negative integers
where its values are stored in **reverse-order** and each of their nodes
contain single digit. Add two numbers and return it as a linked list.

Assume the two numbers do not contain any leading zero, except the number
0 itself.

---

First approach would be to add the numbers as we iterate on the linked lists
and building the result linked list. The carry should be moved over.

Second approach would be to practice a good software engineering principle and
maintain a good readability for the readers. To achieve this, we can divide the
given problem into logical components; 1) convert linked lists into integers,
2) add the two numbers, and 3) convert integers to linked lists.

---

Go: 

```go
func addTwoNumbers(l1, l2 *ListNode) *ListNode {
    var (
        dummyHead := &ListNode{}
        prev := dummyHead
        c := 0
    )
    for l1 != nil or l2 != nil or c != 0 {
        if l1 != nil {
            c += l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            c += l2.Val
            l2 = l2.Next
        }
        c.Next = &ListNode{Val: c%10}
        c = c.Next
        c /= 10
    }
    return dummyHead.Next
}
```

Python:

```python
class Solution:
    def addTwoNumbers(self, l1, l2):
        num1, num2 = self.listToInt(l1), self.listToInt(l2)
        return self.intToList(num1, num2)

    def listToInt(self, head):
        i = 0
        result = 0
        while head:
            result += (head.val * 10 ** i)
            i += 1
        return result

    def intToList(self, num):
        dummyHead = curr = ListNode(None)
        while num:
            curr.next = ListNode(num % 10)
            curr = curr.next
            num //= 10
        return dummyHead.next

```

