""" 496. Next Greater Element I

Question:

    Given two integer arrays where nums1 is subset of nums2, find the next
    greater elements for every element in nums1 that can be found in nums2.

+++

Solution:

    For every element found within the nums1, we could record the next greater
    element values as we iterate on the nums2. This is also achieved by
    utilizing the stack.

    As we iterate on the nums2, we use the stack to perform a stack sort; that
    is, we push in the elements encountered into the stack. But, we do so by
    first recording the contents of the stack as key, and the value as element
    as long as the pop'd element from the stack is LESS than the current element
    encountered. Thus, in the record, we will effectively have all the next
    greater elements stored.

"""

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        record = dict()

        for element in nums2:
            # record next greater elements for each of stack elements which are
            # less than the current element.
            while stack and element > stack[-1]:
                record[stack.pop()] = element
            # push the current element which will also needs to be recorded to
            # find next greater element.
            stack.append(element)

        # for each element found in nums1, we find next greater element
        # according to the record; as a subset the values should exist.
        result = [ record.get(element, -1) for element in nums1 ]
        return result
