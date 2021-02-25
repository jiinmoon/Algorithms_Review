# 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

---

We can solve this problem in linear time complexity as we only have to iterate
on both of the lists; and we can either (1) compute the current digit to place
into current node of the new linked list or, (2) first iterate on both given
lists to retrieve the numbers, add them, and convert them into the linked list
format. In either case, the time complexity remains same but (2) would require
slight more time due to having to iterate the list twice - once to read the
numbers and last to build the result list.

---

Python: Single pass approach.

```python

class Solution2:

    def addTwoNumbers(self, l1, l2):

        if not (l1 or l2):
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
            carry //= 10
            prev = prev.next

        return dummy.next
```

Python: Two pass approach.

```python

class Solution2:

    def listToNum(self, head):

        result = i = 0
        while head:
            result += head.val * 10 ** i
            i += 1
            head = head.next

        return result


    def numToList(self, num):

        if not num:
            return ListNode(0)

        dummy = prev = ListNode(None)

        while num:
            prev.next = ListNode(num % 10)
            prev = prev.next
            num //= 10

        return dummy.next


    def addTwoNumbers(self, l1, l2):

        if not (l1 or l2):
            return l1 or l2

        num1, num2 = self.listToNum(l1), self.listToNum(l2)

        return self.numToList(num1 + num2)
```

Java: Single pass approach.

```java

class Solution2
{
    public ListNode addTwoNumbers(ListNode l1, ListNode l2)
    {
        if (Objects.isNull(l1) || Objects.isNull(l2))
            return (Objects.isNull(l2)) ? l1 : l2;

        ListNode dummy, prev;
        dummy = prev = new ListNode(0);
        int carry = 0;

        while (Objects.nonNull(l1) || Objects.nonNull(l2) || carry > 0)
        {
            if (Objects.nonNull(l1))
            {
                carry += l1.val;
                l1 = l1.next;
            }

            if (Objects.nonNull(l2))
            {
                carry += l2.val;
                l2 = l2.next;
            }

            prev.next = new ListNode(carry % 10);
            carry /= 10;
            prev = prev.next;
        }

        return dummy.next;
    }
}
```
