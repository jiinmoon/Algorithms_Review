Repeated String
===============

The problem breaks down into two cases: does n larger or smaller than the given
length of s?

If the n is smaller than len(s), then we can return the number of 'a's in
s upto index n.

If the n is larger, then we need to multiply the number of 'a's in the s by how
many times that len(s) can fit inside the n plus the 'a's in the s upto the
index of remainder.

---

Python:

```python
def repeatedString(s, n):
    if n < len(s):
        return sum(1 for char in s[:n] if char == 'a')
    total = sum(1 for char in s if char == 'a')
    times, remainder = divmod(n, len(s))
    total = (total * times) + sum(1 for char in s[:remainder] if char == 'a')
    return total
```
