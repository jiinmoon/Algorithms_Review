1152 Analyze User Website Visit Pattern
=======================================

We are given some website visits: the user with name username[i] visited the
website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the
time of their visits.  (The websites in a 3-sequence are not necessarily
distinct.)

Find the 3-sequence visited by the largest number of users. If there is more
than one solution, return the lexicographically smallest such 3-sequence.

---

First, we map each of the users to list of their visited websites as sorted by
its timestamp. Then, we need to create all 3-sequence to user mapping from
these user to websites mapping.

This allows us to find the maximum count of users that visited most popular
3-sequence. With this count, we can return all 3 sequences whose number of
users equal to this maximum count.

Due to way we have to generate all possible 3-sequences in nested fashion, this
is O(n^3) time complexity algorithm.

---

Python:

```python
from collections import defaultdict

class Solution:
    def mostVisitedPattern(self, users, timestamps, websites):
        # create mapping of user : [websites] sorted by time
        userToWebsties = defaultdict(list)
        for _, user, website in sorted(zip(timestamps, users, websites)):
            userToWebsites[user].append[website]
        # generate all 3-sequences mapping to users
        seqToUsers = defaultdict(set)
        for user, w in userToWebsites:
            m = len(webstites)
            for i in range(m-2):
                for j in range(i+1, m-1):
                    for k in range(j+1, m):
                        seqToUsers[(websites[i], websites[j], websites[k])].add(user)
        # find 3-seq that has most users
        maxUserCount = len(max(seqToUsers.values(), key=len))
        return min([seq for seq, users in seqToUsers.items() if len(users) == maxUserCount])
```

