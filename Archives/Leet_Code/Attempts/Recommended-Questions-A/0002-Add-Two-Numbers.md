# 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

---

Since the number represented in the list format starts from least significant
digit, we iterate and add up the values from both lists. At each stage, we
append new node to our result list which sum contains the current digit of the
sum that have been added thus far with modulo operation.

Time complexity and space complexity both are O(m + n).

---

Java:

```java

class Solution {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2)
    {
        if (l1 == null || l2 == null)
            return (l1 != null) ? l1 : l2;

        ListNode dummy, prev;
        dummy = prev = ListNode(0);
        int sum = 0;

        while (l1 != null || l2 != null || sum > 0)
        {
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }
            prev.next = new ListNode(sum % 10);
            sum /= 10;
            prev = prev.next;
        }

        return dummy.next;
    }
}

```

Python:

```python

class Solution:
    def addTwoNumbers(l1, l2):
        if not (l1 and l2):
            return l1 or l2

        dummy = prev = ListNode(None)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            prev.next = ListNode(carry % 10)
            prev = prev.next
            carry //= 10

        return dummy.next

```
