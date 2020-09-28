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

The problem is essentially about our own custom sorting comparator. Given the
log, we first split it into string of words - on the very first word and the
rest of the string. Now, we check the rest of the string to see whether it is
a letter or a digi-logs. As stated in the problem, the letter-logs should come
before the digi-logs, hence, we set the priority of the ordering by first
checking for letter or digi logs, then sort first by the rest of the string and
the head.

---

Python:

```python

class Solution:
    def reorderData(self, logs):
        def logOrder(logs):
            # split into first word and rest of string
            head, rest = logs.split(" ", 1)
            # is it letter logs? then it comes first; then sort alpha
            if rest[0].isalpha():
                return (0, rest, head)
            # else, digi logs does not matter how it is sorted; just comes
            # after above letter logs.
            return (1,)
        return sorted(logs, key=logOrder)
```
