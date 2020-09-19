232 Implement Queue using Stacks
================================

Implement queue using only stacks.

---

The problem lies in the fact that what we need to return as a queue (front
element) would lie at the bottom of the stack. Hence, we will maintain two
queues. When we push, we push onto a single designated "push" stack. When we have
to pop, this is when we start the reverse process and populate the "pop" stack
and return the last element from the "pop" stack.

Since returning the top element can also be a problem, we will maintain
a separate variable to store front of the queue.

---

Python:

```python

class MyQueue:
    def __init__(self):
        self.s1 = list() # push stack
        self.s2 = list() # pop stack
        self.front = None

    def enqueue(self, x):
        if not self.s1:
            self.front = x
        self.s1.append(x)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if self.s2:
            return self.s2[-1]
        return self.front
    
    def empty(self):
        return not (self.s1 or self.s2)
```
