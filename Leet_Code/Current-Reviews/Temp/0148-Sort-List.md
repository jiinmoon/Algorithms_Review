# 148. Sort List

Given the head of a linked list, return the list after sorting it in ascending
order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e.
constant space)?

---

#### 1. Gather nodes in hashmap and sort by keys.

One approach would be to iterate on the given list once and create a hashmap
record of node's value to list of nodes sharing the same value. Here, list is
required as there may be duplicate elements present. We can reuse the same
nodes but due to having to store node's value as a key in hashmap, memory would
be O(n) while O(n * log(n)) for time complexity.

#### 2. Merge Sort.

We can either perform bottom-up or top-down merge sort on the list to solve the
problem in O(n * log(n)) time complexity. As merge sort does not require
additional space, it meets the requirement of O(1) space complexity.

---

Java: Merge-sort.

```java

class Solution148 {
    
    public ListNode sortList(ListNode head)
    {
        if (Objects.isNull(head) || Objects.isNull(head.next))
            return head;
        
        // at each recursion, find the mid way point
        // split the array into two equal halves; join on bottom-up

        ListNode prev = null, newHead = head, fast = head;

        while (Objects.nonNull(fast) && Objects.nonNull(fast.next))
        {
            prev = newHead;
            newHead = newHead.next;
            fast = fast.next.next;
        }
        
        // split the two lists
        prev.next = null;
        ListNode l1 = sortList(head);       // lower half
        ListNode l2 = sortList(slow);       // upper half

        return mergeList(l1, l2);
    }
    
    private ListNode mergeList(ListNode l1, ListNode l2)
    {
        if (Objects.isNull(l1) || Objects.isNull(l2))
            return (Objects.nonNull(l1)) ? l1 : l2;

        ListNode dummy, prev;
        dummy = prev = new ListNode(0);

        while (Objects.nonNull(l1) && Objects.nonNull(l2))
        {
            if (l1.val <= l2.val) {
                prev.next = l1;
                l1 = l1.next;
            } else {
                prev.next = l2;
                l2 = l2.next;
            }
            prev = prev.next;
        }

        prev.next = (Objects.nonNull(l1)) ? l1 : l2;
        
        return dummy.next;
    }
}

```

Python: hashmap + sort keys.

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution148:

    def sortList(self, head: ListNode) -> ListNode:
        
        result = defaultdict(list)
        
        while head:
            result[head.val].append(head)
            head = head.next
        
        dummy = prev = ListNode(None)
        
        for val in sorted(result.keys()):
            for node in result[val]:
                prev.next = node
                prev = prev.next
        
        prev.next = None
        
        return dummy.next
```
