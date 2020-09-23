# 23 Merge K Sorted Lists

We can repeatedly call the merge two function log(K) number of times to
concatenate all together. Since at every level the population of lists drops by
half, it is in fact log(K) in depth.

---

Python:

```python

class Solution:
    def mergeK(self, lists):
        while len(lists) > 1:
            temp = list()
            while lists:
                temp.append(self.mergeTwo(lists.pop(), lists.pop()))
            lists = temp

        return lists[0] if lists else None
```
