# 341. Flatten Nested List Iterator

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be
integers or other lists.

---

Simple process would be to recursively flatten the given nested list. For each
nested object, we find whether it is an integer or another list. If it is
a integer, we can add to our flatten'd list; otherwise, we recursively visit
this list. O(n) in time complexity.

---

Python:

```python

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        self.q = []
        
        def helper(nestedList):
            for nest in nestedList:
                if nest.isInteger():
                    self.q.append(nest.getInteger())
                else:
                    helper(nest.getList())
        
        helper(nestedList)
        
        self.q.reverse()
    
    def next(self) -> int:
        return self.q.pop()
    
    def hasNext(self) -> bool:
         return self.q

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

```
