# 547. Friend Circles

There are N students in a class. Some of them are friends, while some are not.
Their friendship is transitive in nature. For example, if A is a direct friend
of B, and B is a direct friend of C, then A is an indirect friend of C. And we
defined a friend circle is a group of students who are direct or indirect
friends.

Given a N*N matrix M representing the friend relationship between students in
the class. If M[i][j] = 1, then the ith and jth students are direct friends
with each other, otherwise not. And you have to output the total number of
friend circles among all the students.

---

There are two general approaches to this problem: (1) we can use union-find to
union all the friends which belong under a single friend circle; or (2) we use
dfs to discover as far out as possible so long as current friend is not
explored yet.

Using union-find, we create an union structure of simple 1-D array. As we
itereate on the given friend matrix M, we union all the friends that we can
explore while collapsing all the friends that we recorded so far. By using
union-find algorithm, we can complete in O(n^2 * log(n)) as O(n^2) to iterate
on the matrix and for each cell visited, we potentially have to traverse as far
out as O(log(n)) since we are collapsing the travel distance.

---

Python:

```python

class Solution:
    def findCircleNum(self, M):
        m = len(M)

        # assign circle numbers
        union = [i for i in range(m)]
        
        # union all friends under same group
        def unionFind(i):
            while union[i] != i:
                union[i] = union[union[i]]
                i = union[i]
            return i

        # traverse on matrix
        # group each friend together
        for i in range(1, n):
            for j in range(i):
                # i, j are friend
                if M[i][j]:
                    # group together in union
                    # friend i under j
                    union[unionFind(i)] = unionFind(j)

        # count individual friend circles      
        return len(set(unionFind(i) for i in range(m)))
```
