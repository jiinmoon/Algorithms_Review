# First Non-Repeating Character in a Stream of Characters

    Given a string A denoting a stream of lowercase alphabets. You have to make new
    string B.

    B is formed such that we have to find first non-repeating character each time
    a character is inserted to the stream and append it at the end to B. If no
    non-repeating character is found then append '#' at the end of B.

---

## Approach:

Maintain a counter of each character that we encounter. For each character, if
we found that front of our queue is found to be a non-repeat we remove. After
updating queue and counter, if we still have a queue, then we can add front of
our queue to result; otherwise, add "#".

O(n) in both time and space complexity.

---

Python:

```python

from collections import deque, defaultdict

class Solution:

    def firstNonRepeat(self, A):

        queue, counter = deque(), defaultdict(int)
        result = []

        for char in A:
            
            count[char] += 1

            while queue and counter[queue[0]] != 1:
                queue.popleft()

            if queue:
                result.append(queue[0])
            else:
                result.append("#")

        return "".join(queue)
```
