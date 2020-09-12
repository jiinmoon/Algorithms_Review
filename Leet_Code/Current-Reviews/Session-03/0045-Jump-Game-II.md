45 Jump Game II
===============

Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

---

To compute the minimum number of jumps, we repeatedly take the index from range
"start" to "goal". These will initially start at 0, then updated to find the
maximum index that is reachable from that position. In next iteration, the
"start" will be the previous "goal" and the new "goal" should be the maximum
index thus far.

---

C++:

```cpp
class Solution 
{
    public:
        int jump(vector<int>& nums)
        {
            if (nums.size() <= 1) return 0;

            int begin (0), end (0), maxIndexSoFar (0), jumps (1);

            while (1)
            {
                for (int i = begin; i < end+1; ++i)
                    maxIndexSoFar = std::max(maxIndexSoFar, i + nums[i]);

                if (maxIndexSoFar >= nums.size()-1)
                    return jumps;

                jumps++;
                begin = end + 1;
                end = maxIndexSoFar;
            }
            // cannot reach here; algorithm is bound to terminate so long as it
            // is populated by non-negative integers.
        }
};
