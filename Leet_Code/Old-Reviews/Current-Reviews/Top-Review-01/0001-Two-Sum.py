# 1 Two Sum
#
# Naive appraoch involves searching for every possible two element combination
# to see whether they would sum to target value. This nested loop approach is
# O(n^2) in time complexity.
#
# To improve upon this time complexity, we use extra space to store the
# previously seen elements to check against the needed value to sum upto the
# target value. Since hashmap can support this lookup in O(1), the time
# complexity of this algorithm reduces to O(n).

class Solution:
    def findTwoSum(self, nums, target):
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                return [ d[num], i ]
            d[target - num] = i
        return []
