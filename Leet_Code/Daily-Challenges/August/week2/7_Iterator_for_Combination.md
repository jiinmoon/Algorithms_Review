# LeetCode Daily Challenge: August Week.2 - Day.7

## Question

Design an Iterator class, which has:

- A constructor that takes a string characters of sorted distinct lowercase
  English letters and a number combination Length as arguments.

- A function next() that returns the next combination of length
  combinationLength in lexicographical order.

- A function hasNext() that returns True iff there exits a next combination.

## Solution

We may perform precomputation during the init to find and store all the
combinations such that we can improve the time for the returns. There are
several ways: we can either use Backtracking or Bitmasking approach.

There is also an algorithm by Knuth where we will precompute using the
variation on the BFS.

Python:

```python
class Solution:
    def __init__(self, characters, combinationLength):
        self.comb = []
        n, k = len(characters), combinationLength

        # initialize the first combination
        nums = list(range(k)) + [n]

        j = 0
        while j < k:
            # add current combination
            curr = [characters[n - 1 - nums[i]] for i in range(k - 1, -1, -1)]
            self.combinations.append(''.join(curr))

            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j
                j += 1
            nums[j] += 1

    def next(self):
        return self.comb.pop()

    def hasNext(self:
        return self.comb
```

