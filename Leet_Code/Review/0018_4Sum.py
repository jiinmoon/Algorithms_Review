""" 18. 4Sum

Question:

    Find all unique quadruplets in the array that sums to given target.

+++

Solution:

    For any general K-Sum problem, the generic 2Sum algorithm can be used
    effectively. However, with each added elements, it would continue to nest
    our algorithm. Still, we can redue the time complexity utilizing sorting
    method.

    We first sort the array - this has two benefits: (1) we can easily identify
    duplicates and avoid selecting them; (2) give a directionality to use two
    pointer methods.

    Further, we should add improvements on the algorithm via check for boundary
    conditions. We know that at the beginning of each loop, we know the min and
    max - thus, we can avoid spend time in a loop that does not contain any
    answers, yet still iterates along.

"""

class Solution:
    def fourSum(self, nums, target):
        m = len(nums)
        if not nums or m < 4:
            return None
        result = set()
        nums.sort()
        for i in range(m-3):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            if sum(nums[i:i+4]) > target or \
                sum([nums[i], nums[m-1], nums[m-2], nums[m-3]) < target:
                continue
            for j in range(i+1, m-2):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                if sum([nums[i], nums[j], nums[j+1], nums[j+2]) > target or \
                    sum([nums[i], nums[j], nums[m-1], nums[m-2]) < target:
                    continue
                k = j+1
                l = m-1
                while k < l:
                    curr = (nums[i], nums[j], nums[k], nums[l])
                    if sum(curr) == target:
                        result.add(curr)
                        k += 1
                        l += 1
                        while k < l and nums[k-1] == nums[k]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                    elif sum(curr) < target:
                        k += 1
                    else:
                        l -= 1
        return list(result)
