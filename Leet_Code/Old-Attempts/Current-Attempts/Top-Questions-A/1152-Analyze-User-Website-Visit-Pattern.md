# 1152 Analyze User Webstie Visit Pattern

We are given some website visits: the user with name username[i] visited the
website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the
time of their visits.  (The websites in a 3-sequence are not necessarily
distinct.)

Find the 3-sequence visited by the largest number of users. If there is more
than one solution, return the lexicographically smallest such 3-sequence.

---

Firstable, we need to build the list of websites that are visited by an user as
sorted first by the timestamp (user to sorted websites by time). Once we do, we
can create an inverse of this that is the 3 sorted sequences of websites to
a set of users. Then, we find the maximum number of users among them to report
the patterns.

---

Python:

```python

class Solution:
    def mostVisitedPattern(self, users, timestamps, websites):
        userToWebsites = collections.defaultdict(list)
        for _, u, w in sorted(zip(timestamps, users, websites)):
            userToWebsites[u].append(w)

        patternToUsers = collections.defaultdict(set)
        for u, websites in userToWebsites.items():
            m = len(websites)
            for i in range(m-2):
                for j in range(i+1, m-1):
                    for j in range(j+1, m):
                        pattern = tuple(websites[i], websites[j], websites[k])
                        patternToUsers[pattern].add(u)

        maxUserCount = len(max(patternToUsers.values(), key = len))

        return min(pattern for pattern, users in patternToUsers.items() if len(users) == maxUsercount)
```
