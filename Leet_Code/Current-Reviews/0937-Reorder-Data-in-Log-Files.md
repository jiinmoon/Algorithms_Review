973 Reorder Data in Log Files
=============================

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier. Then,
either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is
guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.

The letter-logs are ordered lexicographically ignoring identifier, with the
identifier used in case of ties.  The digit-logs should be put in their
original order.

Return the final order of the logs.

---

It really is about creating a own sorting key. Here, we have our rules:

1. Letter-logs must come before the digits.
2. Letter-logs should be sorted alphanumerically and by its identifier.
3. Digit-logs can stay in its order.

So, we iterate on the array of logs; for each log, we split them into its
identifier and the rest of the content.

If the first char of the rest of the content is a letter, we specify that order
first by its rest, then by its identifier.

If not, then we can specify to do not touch it.

The complexity of the code really depends on the language used here.

---

Python:

```python
class Solution:
    def reorderLogFiles(self, logs):
        def logOrder(logs):
            head, rest = logs.split(" ", 1)
            if rest[0].isalpha():
                # sorting order is Letter-Logs > rest > head
                return (0, rest, head)
            else:
                # Digi-Logs do not require ordering
                # it only needs to come after Letter-Logs
                return (1,)
        return sorted(logs, key = logOrder)
```
