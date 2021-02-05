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

Here, important point is that we do not have to maintain the entire queue at
all - just that whether the given num is unique or not. Hence, we use hashmap
to record each of the numbers to retrieve them; as well, we maintain another
hashmap to check for whether the value is unique or not. Since we need to
retrieve the "first" unique value, the order is also important - so we use
a hashmap that can also maintain an order (such as Python collections Ordered
Dict).

---

Python:

```python

class FirstUnique:
    def __init__(self, nums):
        self.isUnique = dict()
        self.q = collections.OrderedDict()
        for num in nums:
            self.add(num)

    def add(self, num):
        if num not in self.isUnique():
            self.q[num] = None
            self.isUnique[num] = True
        elif self.isUnique[num]:
            self.isUnique[num] = False
            self.q.pop(num)

    def showFirstUnique(self):
        # first value of q is the first unique value since we are removing the
        # non-uniques when duplicate num is added to the queue
        if self.q:
            return next(iter(self.q))
        return -1
```
