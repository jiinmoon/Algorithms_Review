""" 220. Contains Duplicate III

Question:

    Similar set-up; however, now the values should be at most t and indicies at
    most k.

+++

Solution:

    The naive approach would be to iterate on the array to find i and j such
    that while diff between j - i is less than k, we evaluate diff of nums[i] -
    nums[j].

    Better approach would be to use record - hashmap structure to store the
    indicies. This way, we do not have to re-iterate for newly chosen value of
    i, which is a redundant work repeated in naive approach.

"""

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, t, k):
        record = dict()
        for i, thisNum in enumerate(nums):
            for otherNum, j in record.items():
                if abs(thisNum - otherNum) <= t and j - i <= k:
                    return True
            record[thisNum] = i
        return False
