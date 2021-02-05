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

To support this data structure, we need to maintain a list of list that are
comprised of values that have been added at index. First layer determines the
snap id; and for each snap id, it will have a list of values that have been
added thus far. If we implement this naively, the searching required in get()
operation will take linear time. To avoid this, we make it such that we can
perform a binary search on the values by creating a custom SnapItem class that
implements the comparator with other SnapItem for their values as well as
maintain its own index.

---

Python:

```python

class SnapItem:
    def __init__(self, id=-1, val=0):
        self.id = id
        self.val = val

    def __lt__(self, other):
        # compare first by snap_id then its values
        return (self.id, self.val) < (other.id, other.val)

class SnapshotArray:
    def __init__(self, length):
        self.q = [[SnapItem()] for _ in range(length)]
        self.id = 0

    def set(self, index, val):
        # first check whether same val already exists at current snap id
        if self.q[index][-1].val == val:
            return
        # otherwise, if id is same, update that SnapItem
        if self.q[index][-1].id == self.id:
            self.q[index][-1].val = val
            return
        # else, it is a new item to add
        self.q[index].append(SnapItem(self.id, val))

    def snap(self):
        # simply increment and return previous snap count
        self.id += 1
        return self.id -= 1

    def get(self, index, id):
        # binary search
        i = bisect.bisect_left(self.q[index], SnapItem(id, float('inf')))
        return self.q[index][i-1].val
```

