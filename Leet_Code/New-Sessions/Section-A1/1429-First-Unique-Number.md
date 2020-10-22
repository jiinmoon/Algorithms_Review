# 1429 First Unique Number

You have a queue of integers, you need to retrieve the first unique integer in
the queue.

Implement the FirstUnique class:

```
FirstUnique(int[] nums) Initializes the object with the numbers in the queue.

int showFirstUnique() returns the value of the first unique integer of the
queue, and returns -1 if there is no such integer.

void add(int value) insert value to the queue.
```

---

To identify whether the given number in the data structure is unique or not, we
need hashmap. Upon subsequent add of duplicate values, we can mark it as not
unique in O(1) using hashmap.

But the problem is that we need to know which unique value was the "first"
unique value that has been added. To identify this, we need a hashmap where we
can maintain the order - otherwise, we need another queue to maintain the order
for us. In Python, this is achieved with OrderedDict class.

However, we also need a regular hashmap structure to maintain boolean relation
that confirms the uniqueness of the values since duplicate values can be found
more than once. So, we need a complete information.

---

Python:

```python

class FirstUnique:
    def __init__(self, nums):
        self.d = collections.OrderedDict()
        self.isUnique = dict()
        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        if self.d:
            # OrderedDict is not iterable by itself.
            # So, convert to iterable and return first next value in line.
            return next(iter(self.d))
        return -1

    def add(self, num):
        if num not in self.isUnique:
            self.isUnique[num] = True
            self.d[num] = None
        elif self.isUnique[num]:
            self.isUnique[num] = False
            self.d.pop(num)
```
