# 61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

---

To rotate the given linked list, we need to traverse to the Kth node from
behind and adjust the pointers. The next pointer to the Kth node will be our
new head of the list and Kth node will be our new tail.

To do so, we first have to measure the length of the list. It is possible that
k value will be unexpectedly large; thus, we cannot simply traverse to right by
Kth amount. So, we use modulo operation to find the right Kth value that fits
within the range.

Time complexity would be O(n) and O(1) in space complexity.

---

Java:

```java

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution61 {

    public ListNode rotateRight(ListNode head, int k) 
    {
        if (Objects.isNull(head) || Objects.isNull(head.next))
            return head;
        
        ListNode newHead, newTail, curr;
        newHead = newTail = curr = head;
        
        int length = 0;
        for (;Objects.nonNull(curr); 
                curr = curr.next, length++);
        
        k %= length;
        
        for (; k-- > 0; 
                newHead = newHead.next);
        
        for (;Objects.nonNull(newHead.next); 
                newHead = newHead.next, newTail = newTail.next);
        
        newHead.next = head;
        newHead = newTail.next;
        newTail.next = null;
        
        return newHead;
    }
}

```

Python:

```python

class Solution61:

    def rotateRight(self, head, k):
        
        if not (head and head.next and k):
            return head

        def length(node):
            result = 0
            while node:
                node = node.next
                result += 1
            return result

        k %= length(head)

        newHead = newTail = head

        for _ in range(k):
            newHead = newHead.next

        while newHead.next:
            newHead = newHead.next
            newTail = newTail.next

        newHead.next = head
        newHead = newTail.next
        newTail.next = None

        return newHead

```

