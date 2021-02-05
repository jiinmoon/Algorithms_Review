# Partition List

    Given a linked list and a value x, partition it such that all nodes less than
    x come before nodes greater than or equal to x.

    You should preserve the original relative order of the nodes in each of the two
    partitions.

    For example,

    Given 1->4->3->2->5->2 and x = 3,
    return 1->2->2->4->3->5.

---

## Approach:

Prepare a two list where we can store the nodes as we examine; one will store
the values less than x and other greater than or equal to x. At the end, merge
the two lists by concatenating.

O(n) in time complexity.

---

Python:

```python

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def partition(self, A, B):
        
        dummy1 = prev1 = ListNode(None)
        dummy2 = prev2 = ListNode(None)
        
        while A:
            if A.val < B:
                prev1.next = A
                prev1 = prev1.next
            else:
                prev2.next = A
                prev2 = prev2.next
            A = A.next
        
        prev1.next = dummy2.next
        prev2.next = None

        return dummy1.next
```
