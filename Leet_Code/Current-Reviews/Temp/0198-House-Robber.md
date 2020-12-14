# 198. House Robber

You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken
into on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.

---

We can define dp as follows:

    Let DP[i] be maximum profit that can be made upto i-th house. Then we have
    following choices at each i.

        (1) We rob current house.

            If we rob current house, then our max profit will be max profit
            from previous to previous as we had to have skipped the previous
            which is at DP[i-2]. Also, we have to account for current value
            that we have robbed.

        (2) We skip current house.

            If we decide to skip this house, then our max profit will be same
            as previous max profit at DP[i-1].

    In short,

        DP[i] = max(DP[i-2] + nums[i], DP[i-1])

We can improve the space by realizing that we only ever depend upon two
variables; or we could simply reuse the given array. O(n) in time complexity
and O(1) in space.

---

Python:

```python

class Solution198:

    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums) if nums else 0
        
        # we can either rob second house or not
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-1], nums[i-2] + nums[i])
            
        return nums[-1]
```
