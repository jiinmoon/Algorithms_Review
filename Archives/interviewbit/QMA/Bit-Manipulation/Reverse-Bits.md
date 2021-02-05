# Reverse Bits

Reverse the bits of an 32 bit unsigned integer A.

---

Extract a single digit from A, and bitwise OR to result integer. Bitshift A to
left while bitshift result to right. Repeat for 32 times.

O(1) in time and space.

---

Python:

```python

class Solution:

    def reverseBits(self, A):

        result = 0
        for _ in range(A):
            result <<= 1
            result |= A & 1
            A >>= 1

        return result

```
