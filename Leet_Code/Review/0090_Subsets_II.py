""" 90. Subsets II

Question:

    Given a collection of integers that might contain duplicates, nums, return
    all possible subsets. Solution set must not contain any duplicate subsets.

+++

Solution:

    We will start by counting the number of each element in the given list. For
    every element, we need to append this to not only the result set but every
    subset within the result set as well. This is where our count comes into
    account - since the number of times that the element should appear depends
    on the how many time it is present in the given array. 

    Computing a powerset is a exponential operation as it grows rapidly. And
    since we need to go through every subset as well, the time complexity
    should be O(n * 2 ** n).

"""

from collections import Counter

class Solution:
    def powerset_with_dup(self, nums):
        result = [[]]
        counter = Counter(nums)
        for num in counter:
            result += [ subset + [num] * i for i in range(1, counter[num]+1)
                    for subset in result ]
        return result
