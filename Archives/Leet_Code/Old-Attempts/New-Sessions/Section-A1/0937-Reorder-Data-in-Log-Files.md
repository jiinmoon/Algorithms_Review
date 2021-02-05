# 937 Reorder Data in Log Files

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then,
either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is
guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The
letter-logs are ordered lexicographically ignoring identifier, with the
identifier used in case of ties.  The digit-logs should be put in their
original order.

Return the final order of the logs.

---

Most languages should have a sorting library that supports a customized key.
Here, comparator will be implemented to split the given log file, and check for
first letter of the body is alpha or not.

---

Python:

```python

class Solution:
    def reorderLogFiles(self, logs):
        def helper(log):
            head, body = logs.split(" ", 1)
            if body[0].isalpha():
                return (0, body, head)
            return (1,)
        return sorted(logs, key=helper)
```
