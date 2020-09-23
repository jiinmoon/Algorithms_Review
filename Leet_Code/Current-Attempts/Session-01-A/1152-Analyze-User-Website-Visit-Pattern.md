# 1152 Analyze User Website Visit Pattern

Create the user to websites mapping, then create all possible patterns and its
users.

---

Python:

```python

class Solution:
    def analyze(self, users, times, websites):
        userToWebs = collections.defaultdict(list)
        for _, u, w in zip(times, users, websites):
            userToWebs[u].append(w)

        patternToUsers = collections.defaultdict(set)
        for u, webs in userToWebs.items():
            m = len(webs)
            for i in range(m-2):
                for j in range(i+1, m-1):
                    for k in range(j+1, m):
                        pattern = (webs[i], webs[j], webs[k])
                        patternToUsers[pattern].add(u)

        maxUserCount = len(max(patternToUsers.values(), key=len))

        return min(p for p, users in patternToUsers.items() if len(users) == maxUserCount)
```
