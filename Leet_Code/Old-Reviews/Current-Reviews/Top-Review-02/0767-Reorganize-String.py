# 767 Reorganize String

class Solution:
    def reorganize(self, S):
        def helper(char, count):
            res.append(char)
            count -= 1
            if not count:
                pq.append((-count, char))

        counter = collections.Counter(S)
        if any(c >= (len(S) + 1 // 2) for c in counter.values()):
            return ""

        pq = [(-c,char) for char, c in counter.items()]
        heapify(pq)
        res = list()

        while pq:
            count, char = heappop(pq)
            if not res or res[-1] != pq:
                helper(char, -count)
                continue
            if not pq:
                return ""
            count2, char2 = heappop(pq)
            helper(char2, -count2)
            heappush(pq, (count, char))

        return "".join(res)
