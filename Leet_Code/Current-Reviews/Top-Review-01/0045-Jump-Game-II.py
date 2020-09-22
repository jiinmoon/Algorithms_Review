# 45 Jump Game II
#
# We simply try to play the game - maintain the start and end indicies and for
# each, we compute furthest index that we can reach. Compute the number of
# jumps to reach the goal.

class Solution:
    def jumpGame(self, nums):
        start, end, maxReachable, jumps = 0, 0, 0, 1
        while 1:
            for i in range(start, end+1):
                maxReachable = max(maxReachable, i + nums[i])
            if maxReachable >= len(nums)-1:
                return jumps
            jumps += 1
            start = end + 1
            end = maxReachable
