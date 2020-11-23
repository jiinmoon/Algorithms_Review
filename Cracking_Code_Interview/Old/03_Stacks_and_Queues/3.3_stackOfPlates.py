""" 3.3 Stack Of Plates

Question:

    Imagine a literal stack of plates. If the stack gets too high, it might
    topple. Therefore, in real life, we would likely start a new stack when the
    previous stack exceeds some threshold. Implement a data structure
    SetOfStacks that mimics this. SetOfStacks should be composed of several
    stacks and should create a new stack once the previous one xeceeds capacity.
    SetOfStacks.push() and SetOfStacks.pop() should behave identically to a
    single stack.

   Implement a function popAt(int index) which performs a pop operation on a
   specific substack.

---

The question is similar to the MultiStack question that we encountered
beforehand but this time we a bit more practical uses. The idea is to have a
multiple fixed sized stacks that we can grow and shirnk as we peform the
operations.

"""

class MultiStack:

    def __init__(self, stack_size = 10):
        self.stack_size = stack_size
        self.currStack = 0
        self.stacks = [[]]

    def push(self, val):
        if len(self.stacks) :

    def pop(self):


    def popAt(self, stackNum):

