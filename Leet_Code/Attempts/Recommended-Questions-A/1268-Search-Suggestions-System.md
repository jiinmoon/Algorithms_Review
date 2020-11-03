# 1268. Search Suggestions System

Given an array of strings products and a string searchWord. We want to design
a system that suggests at most three product names from products after each
character of searchWord is typed. Suggested products should have common prefix
with the searchWord. If there are more than three products with a common prefix
return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of
searchWord is typed. 

---

Here, we want to return the lexicograpphically minimums products - thus, we
first sort the given products. Then, we examine every prefix generated from the
given searchWord. Since the products are sorted, we can easily find where the
prefix occurs in the products list by using the binary search algorithm. Thus,
if the prefix can be found, we can return the 3 products that share the prefix.

---

Python:

```python

from bisect import bisect_left

class Solution:
    def searchSuggestions(self, products, searchWord):
        products.sort()
        result = list()
        for i in range(1, len(searchWord) + 1):
            prefix = searchWord[:i]
            j = bisect_left(products, prefix)
            result.append([p for p in products[j:j+3] if p[:i] == prefix])
        return result
```
