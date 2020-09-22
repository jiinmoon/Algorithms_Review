# 210 Course Schedule II

class Solution:
    def courseSchedule(self, n, prereqs):
        g = collections.defaultdict(list)
        indeg = [0] * n
        for p, c in prereqs:
            g[p].append(c)
            indeg[c] += 1

        q = collections.deque()
        for i, c in indeg:
            if not c:
                q.append(i)

        res = list()
        while q:
            curr = q.popleft()
            res.append(curr.val)
            for neigh in g[curr]:
                indeg[neigh] -= 1
                if not indeg[neigh]:
                    q.append(neigh)

        return res if not any(indeg) else []
