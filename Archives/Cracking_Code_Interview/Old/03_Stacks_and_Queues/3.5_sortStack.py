""" 3.5 Sort Stack

Question:

    Write a program to sort a stack such that the smallest items are on the top.
    You can use an additional temp stack, but you may not copy the elements into
    any other dat astructure. The stack supports the foolowing: push, pop, peek
    and isEmpty.

---

Prepare two stacks. One stack will act as a 'sorted' stack that will only
contain the values in the correct order whereas the other stack will contain the
original unsorted values. The question is this; how do we place the top of the
'unsorted' stack value into the correct place in the 'sorted' stack?

We repeat the process of until 'unsorted' stack is empty, we check the top of
the 'unsorted' stack value. The temp hold the value after poping it, and pop
from the s2 (and temp place in s1).

"""

class Solution:

    def sortStack(self, unsortedStack):
        if not unsortedStack or len(unsortedStack) <= 1: return unsortedStack

        sortedStack = []
        while !unsortedStack.isEmpty():
            temp = unsortedStack.pop()
            while sortedStack.top() <= temp:
                unsortedStack.push(sortedStack.pop())
            sortedStack.push(temp)

        # need to reverse the list so that min value is on top
        return sortedStack.reverse()

