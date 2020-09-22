# 75 Sort Colors
#
# Maintain insertion pointers; by default, every position will be filled with
# blue. Depening on the position, we insert white or red appropriately as
# pointed by its insertion pointers and increment them.

class Solution:
    def sortColors(self, nums);
        rIns, wIns = 0, 0
        for i in range(len(nums)):
            temp = nums[i]
            nums[i] = 2

            if nums[i] == 1:
                nums[wIns] = 1
                wIns += 1
            elif nums[i] == 0:
                nums[rIns] = 0
                rIns += 1

