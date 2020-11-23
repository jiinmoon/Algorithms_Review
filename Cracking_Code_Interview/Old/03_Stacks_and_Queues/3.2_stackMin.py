""" 3.2 Stack Min

Question:

    How would you design a stack which, in addition to push and pop, has a
    function min which returns the minimum element? Push, pop and min should all
    operate in O(1) time.

---

To design a stack that can support instant look-up of the current min value
inside the stack, we will have to maintain an extra stack within that will keep
track of the only minimum values. This stack will be maintained as we push and
pop.

As we push, we check the top of the minStack, if it is empty or lower, then we
can push onto the minStack.

As we pop, we check the top of the minStack, if the value matches, then we also
pop from the minStack.

"""

class MinStack:
    """ could just extend the Python list """

    def __init__(self):
        self.stack = []
        self.minStack = []

    def pop(self):
        if self.stack.empty():
            """ Should raise empty stack exception """
            return None
        top = self.stack.pop()
        if top == self.minStack.top(): self.minStack.pop()
        return top

    def push(self, val):
        if !self.minStack.empty() or val <= self.minStack.top():
            self.minStack.push(val)
        self.stack.push(val)

    def min(self):
        if self.stack.empty():
            """ Should raise empty stack exception """
            return None
        return self.minStack.top()

