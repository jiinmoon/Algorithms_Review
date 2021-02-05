""" 219. Contains Duplicate II

Question:

    Given an array of integers and an integer k, find out whether there are two
    distinct indicies i and j in the array such that nums[i] = nums[j], and abs
    diff between i and j is at most k.

"""

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        record = dict()
        for i, num in enumerate(nums):
            if num in record and i - record[num] <= k:
                return True
            record[num] = i
        return False
