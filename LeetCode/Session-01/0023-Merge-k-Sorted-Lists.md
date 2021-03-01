# 23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in
ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

---

One intuitive method would be to repeatedly take the first nodes from each of
the linked lists, and find the minimum - then concatenate that current min node
to the new list to be returned.

We can reduce the time complexity by think of this problem as an extension of
merge two linked lists performed over log(k) number of times. The time is
logrithmic since as we merge the two linked lists, we are reducing the size of
total nodes to be merge by half each time - this is akin to calculating the
height of the binary tree.

---

Python:

```python

class Solution23:

    def mergeK(self, lists):

        while len(lists) > 1:
            temp = []

            while lists:
                l1 = lists.pop()
                l2 = lists.pop() if lists else None
                temp.append(self.mergeTwo(l1, l2)

            lists = temp

        return lists[0] if lists else None


    def mergeTwo(self, l1, l2):

        if not (l1 or l2):
            return l1 or l2
        
        dummy = prev = ListNode(None)

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        return dummy.next
```
