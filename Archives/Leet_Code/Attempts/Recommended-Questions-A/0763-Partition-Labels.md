# 763. Partition Labels

A string S of lowercase English letters is given. We want to partition this
string into as many parts as possible so that each letter appears in at most
one part, and return a list of integers representing the size of these parts.

---

To partition the given string S, first we create a mapping of the "last" index
that each of the character appears in. As we iterate on the given string, if
the current index is marked as the last index in the mapping, then we can add
it onto our result.

---

Java:

```java

class Solution {
    public List<Integer> partitionLabels(String S) {
        int[] record = new int[26];
        for (int i = 0; i < S.length(); i++)
            record[(int) S.charAt(i) - (int) 'a'] = i;
        
        List<Integer> result = new ArrayList<>();
        int start, end;
        start = end = 0;
        for (int i = 0; i < S.length(); i++) {
            end = Math.max(end, record[(int) S.charAt(i) - (int) 'a']);
            if (i == end) {
                result.add(end - start + 1);
                start = i + 1;
            }
        }

        return result;
    }
}
```

Python:

```python

class Solution:
    def partitionLabels(self, s):
        counter = {c:i for i, c in enumerate(s)}
        start, end = 0, 0
        result = list()
        for i, c in enumerate(s):
            end = max(end, counter[c])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result
```

