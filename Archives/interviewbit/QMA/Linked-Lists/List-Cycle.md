# List Cycle

Given a linked list, return the node where the cycle begins. If there is no
cycle, return null.

Try solving it using constant additional space.

---

### (1) Set.

Use a set to record the previously seen nodes. When we see that node again, we
know it is the head of where cycle begins. O(n) in both time and space
complexity.

### (2) Floyd's Cycle Detection.

Use a slow and fast runners; fast moves twice as fast. If there isn't a cycle,
they will reach the end of the list. Otherwise, runners will run in a cycle
until both are met. Where they meet will be same distance away from the
beginning of the list. O(n + k) in time complexity where k is the length of the
cycle. O(1) in space.

---

Python: set.

```python

class Solution:

    def detectCycle(self, A):
        
        curr, seen = A, set()

        while curr:
            
            if curr in seen:
                return curr

            seen.add(curr)

        return None
```

Python: Floyd.

```python

class Solution:

    def detectCycle(self, A):

        slow = fast = A

        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                fast = A

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return fast

        return None

```
