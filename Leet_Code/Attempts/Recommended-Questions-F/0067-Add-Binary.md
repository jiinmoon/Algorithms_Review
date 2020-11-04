# 67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

---

Simplest approach would be to convert the binary string into integer format,
then convert their sum back into the binary format.

---

Python:

```python

class Solution:
    def addBinary(self, a, b):
        result = int(a, 2) + int(b, 2)
        return bin(result)[2:] # discard "0b"
```
