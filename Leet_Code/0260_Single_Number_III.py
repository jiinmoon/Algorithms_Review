""" 260. Single Number III """

class Solution:
    def singlenNumber(self, nums):
        record = dict()
        for num in nums:
            if num in record:
                del record[num]
            record[num] = 0
        return list(record.keys())
