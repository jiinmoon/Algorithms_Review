# Add One To Number

    Given a non-negative number represented as an array of digits,

    add 1 to the number ( increment the number represented by the digits ).

    The digits are stored such that the most significant digit is at the head of
    the list.

    Example:

    If the vector has [1, 2, 3]

    the returned vector should be [1, 2, 4]

    as 123 + 1 = 124.


    NOTE: Certain things are intentionally left unclear in this question which you
    should practice asking the interviewer.

    For example, for this problem, following are some good questions to ask :

    Q : Can the input have 0’s before the most significant digit. Or in other
    words, is 0 1 2 3 a valid input?

    A : For the purpose of this question, YES

    Q : Can the output have 0’s before the most significant digit? Or in other
    words, is 0 1 2 4 a valid output?

    A : For the purpose of this question, NO. Even if the input has zeroes before
    the most significant digit.

---

## Approach:

We do not have to try to add and carry over as we expected to. But we notice
that we only have to carry over by 1 when current digit overflows (or is 9).
Hence, we iterate from behind, examining each values. If the value is less than
9, we can simply increment that position by one and return the array.
Otherwise, we continue to set them to zero.

If we find that we have exited the loop, the given array was all 9's. Hence, we
return by creating a new array size + 1 with '1' in front.

We should also take care to remove the leading zeros as specified by the
interviewer note.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def plusOne(self, A):

        for i in range(len(A) - 1, -1, -1):

            if A[i] != 9:
                A[i] += 1
                while A[0] == 0:
                    del A[0]
                return A
            A[i] = 0

        return [1] + A
```
