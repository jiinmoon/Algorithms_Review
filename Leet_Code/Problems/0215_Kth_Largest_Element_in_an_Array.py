""" 215. Kth Largest Element in an Array

Solution:

    Finding Kth largest algorithm is QuickSelect - which utilizes the QuickSort
    algorithm. The idea is as follows:

    Finding Kth Largest within the unsorted array means that finding the Kth
    element from the end on the sorted array - hence, we quicksort, until our
    pivot reaches that k.

"""

from random import shuffle

class Solution:
    def _partition(self, nums, lo, hi, pivot):
        temp = nums[pivot]
        nums[pivot], nums[hi] = nums[hi], nums[pivot]
        i, pivot = lo - 1, hi
        for j in range(lo, hi):
            # if curr element is less than pivot element,
            if nums[j] <= temp:
                # swap to left side of pivot.
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        # place pivot at its rightful place.
        nums[i + 1], nums[pivot] = nums[pivot], nums[i + 1]
        return i + 1 # final pivot index.

    def _quickSelect(self, nums, lo, hi, k):
        # trying to find the k-th largest.
        if lo == hi:
            return nums[lo]
        # ideally, pivot should also be randomized..
        pivot = lo + (hi - lo) // 2
        pivot = self._partition(nums, lo, hi, pivot)
        # now, array is partitioned with pivot at its correct position.
        # we do not have to sort all the way; just left or right of pivot
        # depending on whether k is to left of pivor or right.
        if pivot == k:
            # pivot index is at k-th?
            return nums[k]
        elif k < p:
            # sort lower half of pivot.
            return self._quickSelect(nums, lo, p - 1, k)
        else:
            return self._quickSelect(nums, p + 1, hi, k)

    def findKthLargestElement(self, nums, k):
        # read up on importance of shuffling with quick sort.
        # basically, it avoids the worst case scenario.
        shuffle(nums)
        return self._quickSelect(nums, 0, len(nums) - 1, len(nums) - k)
