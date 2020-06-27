""" Contains Duplicates

Solution:

    To detect whether the array contains any duplicates, we could implement a
    naive solution where we would compare each element against one another. But
    this is an O(n^2) algorithm that can be improved further.

    Another way would be to sort the array, such that we can find the duplicates
    next to one another; but this is bounded by the O of sorting algorithm.

    Then, next approach would be to use an hashmap to count the each element
    present. If the element is already in the set, then we know that is our
    duplicate. This is a linear time solution but also takes O(n) space.

"""

class Solution:
    def containsDuplicates(self, nums):
        if not nums:
            return False
        record = set()
        for num in nums:
            if num in record:
                return True
            record.add(num)
        return False
