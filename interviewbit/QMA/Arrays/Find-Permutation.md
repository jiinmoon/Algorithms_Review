# Find Permutation

Given a positive integer n and a string s consisting only of letters D or I,
you have to find any permutation of first n positive integer that satisfy the
given input string.

D means the next number is smaller, while I means the next number is greater.

Notes

Length of given string s will always equal to n - 1
Your solution should run in linear time and space.

---

Let's break this down into cases:

If current character is "I", then current element has to be in increasing
order. We insert current next minimum value we have left in our candidates.

If current character is "D", then current element has to be in decreasing order
compared to last. we insert current maximum value we have left in our
candidates and perform swap with the last value so that it is decreasing order.

O(n) in time and space complexity.

---

Python:

```python

class Solution:

    def findPermutation(self, n, s):

        result = [0] * len(n)
        result[0] = 1
        
        # maintain min and max values of the candidates to insert
        minVal, maxVal = 2, n

        for i in range(1, n):
            
            # case (1)
            # suppose that we have a permutation upto this point in correct
            # order; then our next value gets the next minimum value in candidates
            if s[i-1] == "I":
                result[i] = minVal
                minVal += 1

            # case (2)
            # to decrease compared to last, we insert maximum value and swap
            # with last position
            else:
                result[i] = maxVal
                maxVal -= 1
                result[i-1], result[i] = result[i], result[i-1]

        return result
```

