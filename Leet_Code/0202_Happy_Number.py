""" 202. Happy Number """

class Solution:
    def isHappyNumber(self, n):
        if not n or n <= 0:
            return False
        record = dict()
        while 1:
            temp = 0
            while n:
                temp += (n % 10) ** 2
                n //= 10
            if temp == 1:
                return True
            if temp in record:
                return False
            else:
                record[temp] = 1
            n = temp
