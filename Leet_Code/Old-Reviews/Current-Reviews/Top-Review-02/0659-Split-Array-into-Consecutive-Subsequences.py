# 659 Split Array into Consecutive Subsequences

class Solution:
    def split(self, nums):
        counter = collections.Counter(nums)
        seq = collections.defaultdict(int)

        for num in nums:
            if not counter[num]:
                continue
            counter[num] -= 1

            if num-1 in seq:
                seq[num-1] -= 1
                seq[num] += 1
            elif counter[num+1] and counter[num+2]:
                counter[num+1] -= 1
                counter[num+2] -= 1
                seq[nums+2] += 1
            else:
                return False

        return True
