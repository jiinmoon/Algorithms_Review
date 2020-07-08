""" 55. Jump Game

Question:

    Given a narray of non-negative integers, you are initially positioned at
    the first index of the array. Each element in the array represetns your max
    jump length at that position. Can you reach to the end?

+++

Solution:

    We would try to simulate the game - at each element, we know how far we can
    jump, thus, we record the furthest index that we can reach for each element
    as we iterate.

"""

class Solution:
    def can_jump(self, nums):
        m = len(nums)
        curr_pos = m - 1
        for i in range(m-1, -1, -1):
            if i + nums[i] >= curr_pos:
                curr_pos = i
        return curr_pos == 0

