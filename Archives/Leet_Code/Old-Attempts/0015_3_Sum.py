""" 15. 3 Sum

Question:

    Given an array nums of n integers, are there elements a, b, c in nums such
    that a + b + c = 0? Find all unique triplets in the array which gives the
    sume of zero.

+++

Solution:

    We may treat this problem as an extension on two sum problem - in fact, any
    K-Sum problem can be viewed as a extension of 2 Sum. We set up an outter
    loop to choose one of the elements, and for each element selected, we may
    use two pointer method to smartly pick the two other values to see whether
    it would sum to zero.

"""

class Solution:
    def findThreeSum(self, nums):
        if not nums or len(nums) < 3:
            return []
        result = []
        nums.sort()
        for i, A in enumerate(nums[:-2]):
            while i > 0 and A == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                curr = (A, nums[j], nums[k])
                if not sum(curr):
                    result.append(list(curr))
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k += 1
                elif sum(curr) < 0:
                    j += 1
                else:
                    k -= 1
        return result
