1268 Search Suggestions System
==============================

Given an array of strings products and a string searchWord. We want to design a
system that suggests at most three product names from products after each
character of searchWord is typed. Suggested products should have common prefix
with the searchWord. If there are more than three products with a common prefix
return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of
searchWord is typed. 

---

Sort the list of products lexicographical order first. Then, for every prefix,
we will perform binary search to find the left most index of the word that
contains that prefix. Then, we put three words in sorted list right of the
index found if its prefix matches the current prefix.

Time complexity should be O(n * log (n)) due to sorting; and if the searchWord
is long we have to add in O(k * log (n)) where k is length of searchWord.

---

Python:

```
from bisect import bisect_left as search

class Solution:
    def suggestedProducts(self, products, searchWord):
        res = []
        products.sort()
        for i in range(1, len(searchWord)+1):
            prefix = searchWord[:i]
            j = search(products, prefix)
            res.append([p for p in products[j:j+3] if p[:i] == prefix])
        return res
```

