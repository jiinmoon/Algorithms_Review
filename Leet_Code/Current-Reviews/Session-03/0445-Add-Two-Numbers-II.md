445 Add Two Numbers II
======================

Given two non-empty linked lists representing two non-negative integers, most
significant digit comes first and each of their nodes contain a single digit.
Add the two numers and return it as a linked list.

---

Simplest approach would be to iterate along both of the lists and retrieve the
numbers first, then use their sum to create a new list to return. While this
method works natively with Python, other langauges will require large type to
be able to store however large the input is going to be to avoid the overflow
issues. If we do not wish to use a library (i.e. Java's BigInteger and etc),
then possible solution is to reverse both of the lists, iterate and sum them
together with carry, then reversing the entire new list to return. Similarly,
stacks can be used to simulate the reversing process.

---

C++: reverse approach.

```cpp
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
    {
        if (!(l1 || l2)) return nullptr;
        if (!(l1 && l2)) return (l1) ? l1 : l2;

        reverseList(&l1);
        reverseList(&l2);

        ListNode* dummy = nullptr, *temp = nullptr;
        int carry = 0;

        while (l1 || l2 || carry)
        {
            if (l1) {
                carry += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                carry += l2->val;
                l2 = l2->next;
            }
            temp = new ListNode(carry % 10);
            temp->next = dummy;
            dummy = temp;
            carry /= 10;
        }
        return dummy;
    }

    void reverseList(ListNode** head)
    {
        ListNode* temp = nullptr, *prev = nullptr;
        ListNode* curr = (*head);
        while (curr)
        {
            temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        (*head) = prev;
    }
};

```

Python: non-reverse, simple iterate forward to retrieve numbers first approach.

```python

class Solution:
    def getNum(node):
        total = 0
        while node:
            total *= 10 + node.val
            node = node.next
        return total

    def addTwoNumbers(l1, l2):
        total = getNum(l1) + getNum(l2)
        
        if not total: return ListNode(0)
        
        # do not forget to reverse the list;
        # here we will simply reverse as we iterate forward
        dummy = None
        while total:
            newNode = ListNode(total % 10)
            newNode.next = dummy
            dummy = newNode
            total //= 10

        return dummy
```
