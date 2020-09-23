# 1268 Search Suggestions System

Sort the products and perform binary search to find the index of where the new
searchWord can be found - here, we return the 3 sorted products starting from
this index if it matches.

---

Python:

```python

class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        res = list()
        for i in range(len(searchWord)):
            prefix = searchWord[:i]
            j = bisect.bisect_left(products, prefix)
            res.append([p for p in products[j:j+3] if p[:i] == prefix])

        return products
```
