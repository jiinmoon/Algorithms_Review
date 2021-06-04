# 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

---

We can add the two numbers represented as a linked list digit by digit as we
iterate forward on both of the list and sum up each digit whilst carrying over
any values overflowed to the next.

This can be done in a single pass along with the computation for current digit
value, or we can factor out to create multiple functions that would first
convert the given linked list into integer format, then convert back the sum of
the two integers into the linked list format.

In either cases, the time complexity would be same; O(n) and no additional
space required other than newly created resulting linked list in O(n).

---

Python:

```python

class Solution2:

    def addTwoNumbers(self, l1, l2):

        if not (l1 and l2):
            return l1 or l2

        dummy = prev = ListNode(None)
        carry = 0

        while l1 or l2 or carry:
            if l1.val:
                carry += l1.val
                l1 = l1.next
            if l2.val:
                carry += l2.val
                l2 = l2.next
            prev.next = ListNode(carry % 10)
            carry //= 10
            prev = prev.next

        return dummy.next
```

Java:

```java

class Solution2 {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2)
    {
        if (Objects.isNull(l1) || Objects.isNull(l2))
            return (Objects.nonNull(l1)) ? l1 : l2;

        ListNode dummy, prev;
        int carry = 0;

        dummy = prev = new ListNode();
        
        while (Objects.nonNull(l1) || Objects.nonNull(l2) || carry > 0)
        {
            if (Objects.nonNull(l1)) {
                carry += l1.val;
                l1 = l1.next;
            }

            if (Objects.nonNull(l2)) {
                carry += l2.val;
                l2 = l2.next;
            }
            
            prev.next = new ListNode(carry % 10);
            prev = prev.next
            carry /= 10;
        }

        return dummy.next;
    }
}
```

