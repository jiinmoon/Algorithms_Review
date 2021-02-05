# First non-repeating character in a stream of characters

Given a string A denoting a stream of lowercase alphabets. You have to make new
string B.

B is formed such that we have to find first non-repeating character each time
a character is inserted to the stream and append it at the end to B. If no
non-repeating character is found then append '#' at the end of B.

---

We use queue to maintain non-repeating characters in front of our queue. When
we encounter new character, we record its count; so long as front of our queue
has count greater than 1, we can remove it. If queue is not empty and
non-repeating character exists, it is in front of queue. Otherwise, we add "#".

O(n) in both time and space complexity.

---

Python:

```python

from collections import deque, defaultdict

class Solution:

    def solve(self, A):

        result = []
        counter = defaultdict(int)
        queue = deque()

        for char in A:
            
            counter[char] += 1

            while queue and counter[queue[0]] > 1:
                queue.popleft()

            if queue:
                result.append(queue[0])
            else:
                result.append("#")

        return "".join(result)
```
