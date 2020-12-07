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

The question is about implementing our own comparator to determine the rank of
two given logs. For each log given, we split to its identifier and words. If we
found that words are letter, then it should come before the digi words.

---

Python:

```python

class Solution937:

    def reorderLogFiles(self, logs):

        def helper(log):
            identifier, words = log.split(" ", 1)
            # is letter log?
            if words[0].isalpha():
                # comes before others
                # within letter logs, are sorted lexicographically
                return (0, words, identifier)
            # otherwise, all digi logs come after letter logs
            return (1,)

        return sorted(logs, key=helper)
```

Java:

```java

class Solution937 {

    public String[] reorderLogFiles(String[] logs)
    {
        Arrays.sort(logs, (log1, log2) -> {
            // place pointer to first char of words
            int i = log1.indexOf(" ") + 1;
            int j = log2.indexOf(" ") + 1;

            boolean isLetter1 = Character.isLetter(log1.charAt(i));
            boolean isLetter2 = Character.isLetter(log2.charAt(j));

            // if both are letter logs, sort lexicographically
            if (isLetter1 && isLetter2) {
                String words1 = log1.substring(i);
                String words2 = log2.substring(j);
                // if there is a tie, sort by entire logs
                if (words1.equals(words2))
                    return log1.compareTo(log2);
                return words1.compareTo(words2);
            } else if (isLetter1 && !isLetter2) {
                return -1;      // sort by log1 first
            } else if (!isLetter1 && isLetter2) {
                return 1;       // sort by log2 first
            } else {
                return 0;       // else tie
            }
        });

        return logs;
    }
}


```
