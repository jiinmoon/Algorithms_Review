Sock Merchant
=============

John works at a clothing store. He has a large pile of socks that he must pair
by color for sale. Given an array of integers representing the color of each
sock, determine how many pairs of socks with matching colors there are.

For example, there are  socks with colors . There is one pair of color  and one
of color . There are three odd socks left, one of each color. The number of
pairs is .

Function Description

Complete the sockMerchant function in the editor below. It must return an
integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock

---

We count up each of the sock by its color. For each count of the socks, we
divide as much as we can to see how many pairs that we can make up.

---

Python:

```python
from collections import Counter

def sockMercahtn(n, ar):
    counter = Counter(ar)
    totalPair = 0
    for count in counter.values():
        times, _ = divmod(count, 2)
        totalPair += times
    return totalpair
```
