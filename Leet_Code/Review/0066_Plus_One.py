""" 66. Plus One

Question:

    Given a non-empty array of digits representing a non-negative integer,
    increment one to the integer.

+++

Solution:

    While we could work with the given format, it would be much easier to
    convert the list into integer, plus one, then format the integer back into
    the list format.

"""

class Solution:
    def list_to_int(self, li):
        result = 0
        for num in li:
            result = result * 10 + num
        return result

    def int_to_list(self, num):
        result = []
        while num:
            result.append(num % 10)
            num //= 10
        return result[::-1]

    def plus_one(self, digits):
        num = self.list_to_int(digits)
        return self.int_to_list(num + 1)
