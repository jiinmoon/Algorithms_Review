# 41 First Missing Positive
#
# We can utilize the fact that first missing positive has to be bounded by the
# length of the given array - as such as use the array itself and indicies as
# a marker for elements present within the array.

class Solution:
    def firstMissingPositive(self, nums):
        nums.append(0)

        for num in nums:
            if num != "#" and num > 0 and num < len(nums):
                nums[num], num = "#", nums[num]

        for i, num in enumerate(nums[1:], 1):
            if num != "#":
                return i

        return len(nums)
