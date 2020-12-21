# 4 Sum

    Given an array S of n integers, are there elements a, b, c, and d in S such
    that a + b + c + d = target? Find all unique quadruplets in the array which
    gives the sum of target.

    Note:

    Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie,
    a ≤ b ≤ c ≤ d)
    The solution set must not contain duplicate quadruplets.

---

## Approach:

To find the quadruplet, we can apply general k-sum finding approach here.
First, sort the array and use two nested loop to determine the outer elements
a and b. Then, we can use two pointers to select c and d in linear time given
that we sort the array first.

O(n^3) in time complexity.

---

Python:

```python

class Solution:

    def fourSum(self, A, B):

        A.sort()
        result = set()

        for i in range(len(A) - 3):
            for j in range(i + 1, len(A) - 2):
                k, l = j + 1, len(A) - 1

                while k < l:
                    
                    curr = (A[i], A[j], A[l], A[k])
                    currSum = sum(curr)

                    if currSum == B:
                        result.add(curr)
                        k += 1
                        l -= 1

                    elif currSum < B:
                        k += 1
                    
                    else:
                        l -= 1

        return sorted(result)
```
