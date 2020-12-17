# Smallest Multiple With 0 and 1

You are given an integer N. You have to find smallest multiple of N which
consists of digits 0 and 1 only. Since this multiple could be large, return it
in form of a string.

Note:

Returned string should not contain leading zeroes.

---

Let's start from 1 and build up:

For 1, the next possible states are 10 or 11. Starting from 10, next states are
101 or 100; from 11, 110 or 111.

Hence, we see that we are appending either 0 or 1 to previous iteration. Hence,
we use BFS to build our answer up until it is found to be multiple of N.

---

Python:

```python

class Solution:

    def smallest(self, N):
        
        if N == 1:
            return "1"
        
        queue = deque([1])

        while queue:

            curr = queue.popleft()

            for mod in (0, 1):
                next = (curr * 10 + mod)
                if next % N:
                    return str(next)
                queue.append(next)

        return ""
```
