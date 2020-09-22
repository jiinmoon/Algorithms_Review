# 767 Reorganize String
#
# To reorganize such that no duplicate elements are next to one another "and"
# extend as far as possible, we simply select the most frequent character first
# and startin appending as far as possible.

import heapq

class Solution:
    def reorganize(self, s):
        def helper(char, count):
            res.append(char)
            count -= 1
            if count:
                heappush(pq, (-count, char))

        counter = collections.Counter(s)

        if any(c >= (len(s) + 1) // 2 for c in counter.values()):
            return ""

        pq = [(-count, char) for char count in counter.items()]
        heapify(pq)

        res = list()
        while pq:
            count, char = heappop(pq)
            if not res or res[-1] != char:
                helper(char, -count)
            if not pq:
                return ""
            count2, char2 = heappop(pq)
            helper(char2, -count2)
            heappush(pq, (count, char))

        return "".join(res)
