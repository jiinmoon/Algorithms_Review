# 1146. Snapshot Array

Implement a SnapshotArray that supports the following interface:

```
SnapshotArray(int length) initializes an array-like data structure with the
given length.  Initially, each element equals 0.

void set(index, val) sets the element at the given index to be equal to val.

int snap() takes a snapshot of the array and returns the snap_id: the total
number of times we called snap() minus 1.

int get(index, snap_id) returns the value at the given index, at the time we
took the snapshot with the given snap_id
```

---

Naive approach would be to use nested list approach where each snap will create
further list down the line. Searching for a value in this case would be
a linear search that can be improved upon further.

To improve our search, we can use the binary search method. To do so, we design
our array such that individual items will contain the id of the snaps and the
value associated with it.

---

Python:

```python

class SnapItem:
    def __init__(self, id=-1, val=0):
        self.id = id
        self.val = val

    def __lt__(self, other):
        return (self.id, self.val) < (other.id, other.val)


class SnapshotArray:
    def __init__(self, length):
        self.q = [[SnapItem()] for _ in range(length)]
        self.id = 0

    def set(self, index, val):
        if self.q[index][-1].val == val:
            return False
        if self.q[index][-1].id == self.id:
            self.q[index][-1].val = val
            return
        self.q[index].append(SnapItem(self.id, val))

    def snap(self):
        self.id += 1
        return self.id - 1

    def get(self, id, index):
        i = bisect.bisect_left(self.q[index], SnapItem(id, float('inf')))
        return self.q[index][i-1].val
```
