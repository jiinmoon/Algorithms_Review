""" 3.4 Queue via Stacks

Question:

    Implement a MyQueue class which implements a queue using two stacks.

---

Thie is a fundamental question that asks for understand of difference between
LIFO and FIFO operations of Queue and Stack.

Queue is a FIFO structure; just a simple orderly line at a fast food joint.

Stack is a LIFO structure; stack of plates being served.

The answer lies within the question itself when it says that we can use two
stacks to implement the queue.

Suppose we enqueue three numbers 1, 2, and 3. One stack would look like this:

    3   |
    2   |
    1   |


Now, to access the very first element in queue which is 1, we will have to pop
three times. As we pop, we push those elements unto the other stack.

    1   |   2
        |   3

Thus, the idea is to use the second stack as a mean to reverse the operations to
fit the queue. However, if this has to be repeated for every peek, and pop, then
this can become costly. Thus, we approach the problem in lazy fashion where we
would defer reversing the operations unless we are forced to do so.

So, when we are adding to the queue, we push to first stack as normally. When
peek or pop is called, first we check whether second stack is empty or not. The
top of the second stack will always be the first to go out in queue. If it is
empty, it is time to reverse the contents of the first stack unto the second
stack.

"""

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, val):
        """ stack1 always takes in new values """
        self.stack1.push(val)

    def _reverseStack(self):
        """ shift only when stack2 is empty """
        if self.stack2.isEmpty():
            while !self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())

    def peek(self):
        self._reverseStack()
        return self.stack2.top()

    def dequeue(self):
        self._reverseStack()
        return self.stack2.pop()

