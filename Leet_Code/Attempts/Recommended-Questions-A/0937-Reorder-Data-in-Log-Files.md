# 937. Reorder Data in Log Files

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

For this problem, we create our own customized comparator function to be used
with the sorting algorithm. Here, comparator takes in the individual log. The
log is split into first word and the rest of the word. Based on the identifier,
the log order is determined.

---

Java:

```java

class Solution {

    public String[] reorderLogFiles(String[] logs) {
        Arrays.sort(logs, (log1, log2) -> {
            // split log into head and rest by first separator
            int i = log1.indexOf(" ");
            int j = log2.indexOf(" ");

            // i, j are heads of the rest
            boolean isLetter1 = Character.isLetter(log1.charAt(i+1));
            boolean isLetter2 = Character.isLetter(log2.charAt(j+1));

            // three cases:
            // (1) both are letter-logs
            // (2) log1 is letter-log
            // (3) log2 is letter-log
            if (isLetter1 && isLetter2) {
                // both are logs; compare rest ordering first
                String rest1 = log1.substring(i);
                String rest2 = log2.substring(j);
                // if rests are same, order by entire list instead
                return (!rest1.equals(rest2)) ? 
                            rest1.compareTo(rest2) : 
                            log1.compareTo(log2);
            } else if (isLetter1 && !isLetter2) {
                // letter-log before digi-log
                return -1;
            } else if (!isLetter1 && isLetter2) {
                return 1;
            } else {
                return 0;
            }
        });

        return logs;
    }
}
```

Python:

```python

class Solution:
    def reorderLogFiles(self, logs):
        def helper(log):
            head, rest = log.split(" ", 1)
            if rest[0].isalpha():
                return (0, rest, head)
            return (1,)
        return sorted(logs, key=helper)
```
