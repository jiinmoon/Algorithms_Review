""" 228. Summary Ranges

Question:

    Given a sorted integer array without duplicates, return the sumary of its
    ranges.

"""

class Solution:
    def summarizeRanges(self, nums):
        result = []
        i = 0
        while i < len(nums):
            j = i + 1
            prev = nums[i]
            # move forward until next is in range.
            while j < len(nums) and prev + 1 == nums[j]:
                prev = nums[j]
                j += 1
            # single case.
            if nums[i] == prev:
                temp = str(prev)
            # multiple ranges found.
            else:
                temp = '{}->{}'.format(nums[i], prev)
            result.append(temp)
            i = j
        return result
