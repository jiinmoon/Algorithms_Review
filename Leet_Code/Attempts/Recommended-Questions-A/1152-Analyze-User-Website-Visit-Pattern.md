# 1152. Analyze User Website Visit Pattern

We are given some website visits: the user with name username[i] visited the
website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the
time of their visits.  (The websites in a 3-sequence are not necessarily
distinct.)

Find the 3-sequence visited by the largest number of users. If there is more
than one solution, return the lexicographically smallest such 3-sequence.

---

The end goal is to find the pattern that shares the largest number of users. To
do so, we would first create a mapping between each of the users to websites
that the user have visited. From this mapping, we can iterate to generate all
possible 3-sequence pattern, and create a new mapping between the pattern and
the users that shares the same patterns. Here, we can finally find the maximum
number of users for any particular pattern and return the patterns that shares
the same maximum number of users found.

---

Python:

```python

class Solution:
    def mostVisitedPatttern(self, users, timestamps, websites):
        usersToWebsites = collections.defaultdict(list)
        for _, user, website in sorted(zip(timestamps, users, websites)):
            usersToWebsites[user].append(website)

        patternToUsers = collections.defaultdict(set)
        for user, websites in usersToWebsites.items():
            m = len(websites)
            for i in range(m-2):
                for j in range(i+1, m-1):
                    for k in range(j+1, m):
                        pattern = [websites[i], websites[j], websites[k]]
                        patternToUsers[pattern].add(user)

        maxUserCount = len(max(patternToUsers, key=len))
        return [p for p, u in patternToUsers.items() if len(u) == maxUserCount]
```
