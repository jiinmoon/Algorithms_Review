# 819. Most Common Word

Given a paragraph and a list of banned words, return the most frequent word
that is not in the list of banned words.  It is guaranteed there is at least
one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of
punctuation.  Words in the paragraph are not case sensitive.  The answer is in
lowercase.

---

The first problem that we encounter here would be to sanitizing the
non-character values to split the given paragraph into list of words. This can
be done with the regex substitution of replacing any non-character(not
A-Za-z0-0) with a whitespace. And then spliting the clean string by the
whitespace characters. Once we have the list of words, we can create the
counter mapping of word to count while checking that each word is not in the
list of banned words.

---

Java: iterate char-by-char approach;

Things to note here:

(1) Converting to char array, and accessing via indexing is faster than
repeatedly calling String.charAt(int) function. This will take more space but
is worth it most of time.

(2) StringBuilder is better in general compared to using string concatenation
operation.

```java

class Solution {

    public String mostCommonWord(String paragraph, String[] banned)
    {
        char[] paragraphChars = paragraph.toCharArray();
        Set<String> bannedWords = new HashSet<>(Arrays.asList(banned));
        Map<String, Integer> counter = new HashMap<>();
        
        StringBuilder currWord = new StringBuilder();
        String result = "";
        int maxCount = 0;

        for (int i = 0; i < paragraphChars.length(); i++)
        {
            char currChar = paragraphChars[i];

            // 1. current char is A-Z, a-z, 0-9; add to current word to build
            if (Character.isLetter(currChar))
            {
                currWord.append(Character.toLowerCase(currChar));
                // we may forget the last word (i.e. "Bob")
                // hence, stop only when index has not reached the end;
                if (i != paragraphChars.length() - 1)
                    continue;
            }

            // 2. is a break-point and word has been found
            if (currWord.length() > 0)
            {
                String curr = currWord.toString();
                if (!bannedWords.contains(curr))
                {
                    int currCount = counter.getOrDefault(curr, 0);
                    if (currCount > maxCount) {
                        maxCount = currCount;
                        result = curr;
                    }
                    counter.put(curr, currCount + 1);
                } 
                currWord = new StringBuilder();
            }
        }

        return result;
    }
}

```

Python: regex approach;

```python

import re

class Solution:
    def mostCommonWords(self, paragraph, banned):
        banned = set(banned)
        banned.add("")
        words = re.sub("[^A-Za-z0-9]", " ", paragraph).lower().split(" ")
        counter = collections.Counter([word for word in words if word not in banned])
        return max(counter.items(), key=x : x[1])[0] 
```
