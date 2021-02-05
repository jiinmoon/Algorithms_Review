1429 First Unique Number
========================

You have a queue of integers, you need to retrieve the first unique integer in
the queue.

Implement the FirstUnique class:

- FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
- int showFirstUnique() returns the value of the first unique integer of the
  queue, and returns -1 if there is no such integer.
- void add(int value) insert value to the queue.

---

Naive approach would require no extra data structure but just have a queue and
search the frequency to find the first unique integer. Since for each item in
queue, we need to count up - worst case it will be O(n^2) in time complexity to
find the first unique number.

Improvement would be using a separate hashmap for unique values that can be
easily returned when showFirstUnique is called.

When we add in a new value to the queue, we can first check whether the element
exists in the hashmap. If not, then it is clear that it is the unique value, and
we can mark it as such by putting into the hashmap indicator. If found, then
this element is no longer the unique element - we mark it false in hashmap, and
remove from the queue since we do not need it! All we need is to indicate
whether a number that was placed on the queue was unique. We do not need to
needlessly store the data.

To support this, our queue also has to support remove at a place where value
lies in contant time to be efficient. A set structure implemented with a doubly
linked list could do it; but in python, we can use OrderedDict from
collections.

This improved method can support adding, and showFirstUnique in constant time
- we just takes O(n) for n number of values that are given at the
  initialization.

---

Python: Naive Approach

```python
class FirstUnique:
    def __init__(self, nums):
        self.q = nums

    def showFirstUnique(self):
        for num in self.q:
            if self.q.count(num) == 1:
                return num
        return -1

    def add(self, val):
        self.q.append(val)
```

Python: Improved using OrderedDict and Hashmap

```python
from collections import OrderedDict

class FirstUnique:
    def __init__(self, nums):
        self.unique = dict()
        self.q = OrderedDict()

    def add(self, val):
        if val not in self.unique:
            self.unique[val] = True
            self.q[val] = None
        elif self.unique[val]:
            self.unique[val] = False
            self.q.pop(val)
    
    def showFirstUnique(self):
        if self.q:
            # note here is that we can convert the OrderedDict into list then
            # get the first element. But doing so will first populate all the
            # list before we can index it.
            # this approach is better
            # https://stackoverflow.com/questions/21062781/shortest-way-to-get-first-item-of-ordereddict-in-python-3.
            return next(iter(self.q))
```
