""" 229. Majority Element II

Solution:

    The question gives us hint that the answer has upto two answers since the
    elements has to appear more than floor(n / 3).

    Then, it is a matter of finding the two elements; we will use majority
    voting algorithm to determine this. As we iterate on the array, we keep
    track of first, and second most frequent elements by keeping track of these
    elements count. We could simply count the every element, but this saves
    space.

    While the algorithm does find two most frequently appearing elements if
    possible, it does not unfortunately gives us their actual count to see
    whether it meets the criteria of appearing more than floor(n /3). Thus, we
    will iterate once more to count the elements found.

"""

class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []

        first, second = float('-inf'), float('-inf')
        firstCount, secoundCount = 0, 0

        # find two most frequently appearing element.
        for num in nums:
            if first == num:
                firstCount += 1
            elif second == num:
                secoundCount += 1
            elif firstCount == 0:
                first = num
                firstCount = 1
            elif secoundCount == 0:
                second = num
                secondCount = 1
            else:
                firstCount -= 1
                secondCOunt - =1

        # reset counts; recount the actual amount.
        firstCount, secoundCount = 0, 0
        for num in nums:
            if first == num: firstCount += 1
            if second == num: secoundCount += 1

        if firstCount > len(nums) // 3:
            result.append(first)

        # second may or may not exist.
        if secoundCount > len(nums) // 3 and first != second:
            result.append(second)

        return result
