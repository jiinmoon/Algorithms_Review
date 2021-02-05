# 689. Maximum Sum of 3 Non-overlapping Subarrays

In a given array nums of positive integers, find three non-overlapping
subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k
entries.

Return the result as a list of indices representing the starting position of
each interval (0-indexed). If there are multiple answers, return the
lexicographically smallest one.

---

To find all the subarray of size k where each of the subarray are
non-overlapping and maximized, we create 3 subarraies of each size k and
maintain its maximum sum thus far.

Hence, whenever we iterate on the given array nums, we consider adding the
current value onto the each of the subarrays created (which are first
initialized into subarrays stacked next to each other consecutively from
starting index 0) and remove the last element (first in the window).

Then, we we discover that each current window sum after updating with the
current value is greater than the previous sum, then we have a potential
maximum subarray found. We update the maximum subarray sum found thus far for
each of the subarrays 1, 2, and 3; and record the starting indicies of each of
the subarrays.

The time complexity should be O(n).

---

Python:

```python

class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        # initialize each subarray windows sum
        currFirstSum = sum(nums[:k])
        currSecondSum = sum(nums[k:k*2])
        currThirdSum = sum(nums[k*2:k*3])

        # maintain and record maximum sum found thus far
        maxFirstSum = currFirstSum
        maxSecondSum = currFirstSum + currSecondSum
        maxThirdSum = currFirstSum + currSecondSum + currThirdSum

        # record sarting indicies of subarrays where their sum is the max thus far
        maxFirstIndex = 0
        maxSecondIndex = [0, k]
        maxThirdIndex = [0, k, k * 2]

        # next value and its index to consider for each windows
        i, j, l = 1, k + 1, k * 2 + 1

        while k <= len(nums) - k:
            # update current windows sum by adding current and remove last
            currFirstSum += nums[i + k - 1] - nums[i - 1]
            currSecondSum += nums[j + k - 1] - nums[j - 1]
            currThirdSum += nums[l + k - 1] - nums[l - 1]

            # update maximum sums for each windows and its starting indicies
            if currFirstSum > maxFirstSum:
                maxFirstSum = currFirstSum
                maxFirstIndex = i

            if maxFirstSum + currSecondSum > maxSecondSum:
                maxSecondSum = maxFirstSum + currSecondSum
                maxSecondIndex = [maxFirstIndex, j]

            if maxSecondSum + currThirdSum > maxThirdSum:
                maxThirdSum = maxSecondSum + currTirdSum
                maxThirdIndex = [maxFirstIndex, j, l]

            i += 1
            j += 1
            l += 1

        return maxThirdIndex
```


