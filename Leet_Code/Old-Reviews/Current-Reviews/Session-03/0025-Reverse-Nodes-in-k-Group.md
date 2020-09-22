25 Reverse Nodes in k Group
===========================

Given a linked list, reverse the nodes of a linked list k at a time and return
its modified list.

k is a positive integer and is less tha nor equal to the length of the linked
list. If the number of nodes is not a multiple of k then left-out nodes in the
end should remain as is.

---

We use recursion - first, we detect whether there are enough nodes to make
a k-groupings; on every k-th node, we recurse to identify all k-groups.

Then, on the way out of recursion, we reverse all the k-group nodes.

Time complexity should be linear.

---

C++:

```cpp
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k)
    {
        if (!head || k < 2) return head;

        ListNode* curr = head;
        for (int i = 0; i < k; ++i) {
            if (!curr) return head;
            curr = curr->next;
        }

        ListNode* prev = self.reverseKGroup(curr, k);

        ListNode* temp;
        for (int i = 0; i < k; ++i) {
            temp = head->next;
            head->next = prev;
            prev = head;
            head = temp;
        }

        return prev;
    }
};
```
