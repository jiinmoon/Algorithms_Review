# 981. Time Based Key Value Store

Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.

2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp\_prev) was called
previously, with timestamp\_prev <= timestamp.

If there are multiple such values, it returns the one with the largest
timestamp\_prev.

If there are no values, it returns the empty string ("").

---

We can use hashmap to store the pair of (timestamp, value). For get operation,
we perform binary search to find the matching or rightmost matching pair of
timestamp.

O(log(n)) for get(); O(1) for set().

---

Python:

```python

from collections import defaultdict

class TimeItem:

    def __init__(self, timestamp=None, value=None):
        self.timestamp = None
        self.value = None

    def __lt__(self, other):
        return self.timestamp < other.timestamp


class Solution981:

    def __init__(self):

        self.d = defaultdict(list)


    def set(self, key, value, timestamp):

        self.d[key].append(TimeItem(timestamp, value))


    def get(self, key, timestamp):

        i = bisect_right(self.d[key], TimeItem(timestamp, None))
        return self.d[key][i - 1].value if i else ""

```
