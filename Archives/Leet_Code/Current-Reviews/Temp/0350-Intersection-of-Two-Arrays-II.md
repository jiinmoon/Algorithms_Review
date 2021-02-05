# 350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

---

Here, the point is that intersection does not necessarily have to appear in the
order; hence, we can forgo nested loop to search from every intersection's
start. Rather, we can use hashmap to count values from one, and check against
another.

---

Python:

```python

class Solution350:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        
        counter = Counter(nums1)
        
        # reusing same list given
        i = 0
        for num in nums2:
            if num in counter and counter[num] > 0:
                counter[num] -= 1
                nums1[i] = num
                i += 1
        
        return nums1[:i]
```
