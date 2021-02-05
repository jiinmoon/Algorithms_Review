# Gray Code

    The gray code is a binary numeral system where two successive values differ in
    only one bit.

    Given a non-negative integer n representing the total number of bits in the
    code, print the sequence of gray code. A gray code sequence must begin with 0.

    For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

    00 - 0
    01 - 1
    11 - 3
    10 - 2

    There might be multiple gray code sequences possible for a given n.

    Return any such sequence.


---

## Approach:

Let's try first few sequences and derive a pattern.

    1       0       ->          0
    2       1       ->          1
    3       11      ->          3
    4       10      ->          2

We find that for every iteration, we are expanding previous result with either
"0" or "1". Hence, we build upon previous result where we append the extra bits
as we iterate forward to n.

O(2^n) in both time and space complexity as we are doubling the size of the
result.

---

Python:

```python

class Solution:

    def grayCode(self, n):

        result = [0]

        for i in range(n):
            result += [r + 2 ** i for r in result[::-1]]

        return result
```
