# 763. Partition Labels

A string S of lowercase English letters is given. We want to partition this
string into as many parts as possible so that each letter appears in at most
one part, and return a list of integers representing the size of these parts.

---

We first create a character index mapping where we record the index of
characters where they "last" appears.

Then, as we iterate on each of the charcter in the given string S, if we found
that this is a last character that should appear in the result, a new partition
has been found - we record its length to our result and update our starting
position of new partition point as current index.

This would be O(n) in time complexity and O(n) in space complexity as char
index mapping would be constant `sizeof(int) * 26`, but we have to build our
result list.

---

Java:

```java

class Solution763 {

    public List<Integer> partitionLabels(String S)
    {
        int[] charIndex = new int[26];
        int[] chars = S.toCharArray();
        for (int i = 0; i < chars.length; i++)
            charIndex[chars[i] - 'a'] = i;

        List<Integer> result = new ArrayList<>();
        int start = 0, end = 0;

        for (int i = 0; i < chars.length; i++)
        {
            end = Math.max(end, charIndex[chars[i]]);
            // current character is the last to appear at current index
            if (end == i)
            {
                result.add(end - start + 1);
                // start a new partition
                start = i + 1;
            }
        }

        return result;
    }
}

```
