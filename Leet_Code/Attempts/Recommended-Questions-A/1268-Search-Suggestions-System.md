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

Another method would be to use max-heap to maintain our list of products that
have matched the prefix thus far in the order; - at the end of each search, we
add the contents of our max-heap to our result.

In both cases, sorting is involved (in the case of max-heap, it is practically
a heap-sort). Hence, the time complexity is O(n * log(n)) and space complexity
is O(n) for result to build.

---

Java: heap method.

```java

class Solution {

    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        
        PriorityQueue<String> pq = new PriorityQueue<>(Collections.reverseOrder());
        List<List<String>> result = new LinkedList<>();
        
        // generate every prefix and find three suggested products
        for (int i = 1; i < searchWord.length() + 1; i++) {
            String prefix = searchWord.substring(0, i);
            for (String product : products) {
                if (product.startsWith(prefix))
                    pq.add(product);
                if (pq.size() > 3)
                    pq.remove();
            }
            LinkedList<String> temp = new LinkedList<>();
            while (!pq.isEmpty())
                temp.addFirst(pq.remove());
            result.add(temp);
        }
        
        return result;
    }
}

```

Python: binary search method;

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
