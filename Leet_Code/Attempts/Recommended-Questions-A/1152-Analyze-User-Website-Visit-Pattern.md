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

Time and space complexity would be O(n^3) for all patterns generated.

---

Java:

```java

import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;

class Solution {
    
    // Triplet stores set of (time, user, website)
    static class Triplet implements Comparable<Triplet> {
        private String user;
        private String website;
        private int time;

        public Triplet(String user, String website, int time) {
            this.user = user;
            this.website = website;
            this.time = time;
        }

        @Override
        public int compareTo(Triplet other) { 
            return Integer.compare(this.time, other.time);
        }
    }

    public List<String> mostVisitedPattern(String[] username, int[] timestamp, String[] website) {
        // collect Triplets
        List<Triplet> triplets = new LinkedList<>();
        for (int i = 0; i < timestamp.length; i++)
            triplets.add(new Triplet(username, website, timestamp);

        // sort by time
        Collections.sort(triplets);

        // create user to websites mapping
        Map<String, List<String>> userToWebsites = new HashMap<>();
        for (Triplet t : triplets) {
            String user = t.user;
            String website = t.website;

            List<String> websites = userToWebsites.getOrDefault(user, new LinkedList<>());
            websites.add(website);
            userToWebsites.put(user, websites);
        }

        // generate all patterns and create pattern to users mapping
        Map<List<String>, Set<String>> patternToUsers = new HashMap<>();
        for (String user : userToWebsites.keySet()) {
            List<String> websites = userToWebsites.get(user);
            int m = websites.size();
            for (int i = 0; i < m-2; i++) {
                for (int j = i+1; j < m-1; j++) {
                    for (int l = j+1; k < m; k++) {
                        List<String> pattern = List.of(websites.get(i), websites.get(j), websites.get(k));
                        Set<String> users = patternToUsers.getOrDefault(pattern, new HashSet<>());
                        users.add(user);
                        patternToUsers.put(pattern, users);
                    }
                }
            }
        }

        // determine maximum user count to find most visited patterns
        int maxUserCount = 0;
        for (Set<String> users : patternToUsers.values())
            maxUserCount = Math.max(maxUserCount, users.size());

        // collect all patterns of most visited
        // if there are multiple of them, find lexicographically sorted order
        List<List<String>> result = new LinkedList<>();
        for (List<String> pattern : patternToUsers.keySet()) {
            Set<String> users = patternToUsers.get(pattern);
            if (users.size() == maxUserCount)
                result.add(pattern);
        }
        
        Collections.sort(result, (pattern1, pattern2) -> {
            for (int i = 0; i < 3; i++) {
                String web1 = pattern1.get(i);
                String web2 = pattern2.get(i);
                int cmp = web1.compareTo(web2);
                if (cmp != 0) return cmp;
            }
            return 0;
        });

        return result.get(0);
    }
}

```

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
