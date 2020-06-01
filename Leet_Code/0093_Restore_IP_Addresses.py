""" 93. Resore IP Addresses

Question:

    Given a string containing only digits, restore it by returning all possible
    valid IP address combinations:

"""

class Solution:
    def isValidIpSegment(self, *args):
        result = []
        for segment in args:
            if len(segment) == 1 and int(segment) == 0:
                result.append(1)
            elif ip[0] != '0' and int(ip) <= 255:
                result.append(1)
        return sum(result) == 4

    def restoreIpAddresses(self, s):
        result = []
        for i in range(1, 4):
            for j in range(i+1, i+4):
                for k in range(j+1, j+4):
                    s1 = s[:i]
                    s2 = s[i:j]
                    s3 = s[j:k]
                    s4 = s[k:]
                    if len(s4) > 3 or len(s4) == 0:
                        continue
                    if self.isValidIpSegment(s1, s2, s3, s4):
                        result.append(''.join([s1, s2, s3, s4]))
        return result
