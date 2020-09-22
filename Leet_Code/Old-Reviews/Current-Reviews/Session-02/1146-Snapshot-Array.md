1146 Snapshot Array
===================

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

Naively, we could simply maintain an array, and a record of all this array
whenever we take a snapshot in a hashmap structure. However, this is
unsatisfactory approach as this implies that whenever snap is called, we copy
entire current array and store them; this takes too long.

Better approach would be to maintain an array of tuples where each indicies
will store the (snapshot id, value); hence, only include the values that has
been set instead of entire array compared to naive approach.

This will ensure O(1) in both set and snap. The get operation however can be
slow due to having to iterate to find the matching value with given snapshotId
on the index. To avoid this, we perform binary search for snapshotId value. 

---

Python: naive approach (times-out).

```python
class SnapshotArray:
    def __init__(self, length):
        self.A = [ 0 for _ in range(length) ]
        self.snapId = 0
        self.d = dict()

    def set(self, index, val):
        self.A[index] = val

    def snap(self):
        self.d[self.snapId] = self.A.copy()
        self.snapId += 1
        return self.snapId - 1
    
    def get(self, index, snap_id):
        if snap_id in self.d:
            return self.d[snap_id][index]
        return self.A[index]

```

Python: binary-search approach for get().

```python
class SnapItem:
    def __init__(self, snapshotId=-1, val=0):
        self.item = (snapshotId, val)
        self.snapshotId = snapshotId
        self.val = val
    
    def __lt__(self, other):
        return self.item < other.item

    def setVal(self, val):
        self.item = (self.snapshotId, val)
        self.val = val

class SnapshotArray:
    def __init__(self, length: int):
        # each index is a list of (snapshotId, value)
        self.history = [ [SnapItem()] for _ in range(length) ]
        self.snapshotId = 0
        
    def set(self, index: int, val: int) -> None:
        # same value already in that index
        if val == self.history[index][-1].val: return
        # if id is same, update the value
        if self.history[index][-1].snapshotId == self.snapshotId:
            self.history[index][-1].val = val
            return
        # else new val to add
        self.history[index].append(SnapItem(self.snapshotId, val))
        
    def snap(self) -> int:
        self.snapshotId += 1
        return self.snapshotId - 1

    def get(self, index: int, snap_id: int) -> int:
        # find insertion point for SnapItem with same snapId;
        # it should be right of the matching snap_id
        i = bisect.bisect_left(self.history[index], SnapItem(snap_id, float('inf')))
        return self.history[index][i-1].val
```

