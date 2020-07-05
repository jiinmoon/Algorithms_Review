""" 38. Count and Say

Question:

    Given n <= 30, generate nth term of the count-and-say sequence.

+++

Solution:

    We would simply need to generate the count-and-say sequence these sequences
    build upon one another. Hence, we expect a O(n) time complexity. If we
    think that this function is going to be called often, since we have
    a gurantee that n <= 30, we should generate themm all once, and then store
    them in cache for fast retrieval.

"""

class Solution:
    def count_and_say(self, n):
        if n <= 0:
            return ''
        if n == 1:
            return '1'
        prev = '1'
        while n > 1:
            i = 0
            curr = ''
            while i < len(prev):
                j = i + 1
                while j < len(prev) and prev[i] == prev[j]:
                    j += 1
                curr += str(j - i) + prev[i]
                i = j
            prev = curr
            n -= 1
        return prev
    

