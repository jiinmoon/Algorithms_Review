# 809. Expressive Words

Sometimes people repeat letters to represent extra feeling, such as "hello" ->
"heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have
groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal
to S by any number of applications of the following extension operation: choose
a group consisting of characters c, and add some number of characters c to the
group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o"
to get "hellooo", but we cannot get "helloo" since the group "oo" has size less
than 3.  Also, we could do another extension like "ll" -> "lllll" to get
"helllllooo".  If S = "helllllooo", then the query word "hello" would be
stretchy because of these two extension operations: query = "hello" ->
"hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

---

To find whether the given word can be "stretched" to form the expressive words,
we first create a ordered list of characters and its counts. Then, for each
word that we examine, we should first check for whether correct order of the
characters are present. Then, we take a look at each of the counts from the
word and the string to see whether it fits the criteria of being expressive.

---

Python:

```python

class Solution:
    def expressiveWords(self, words, S):
        def helper(word):
            chars, counts = list(), list()
            count = 1
            for i, char in enumerate(word):
                if i == len(word) - 1 or char != word[i+1]:
                    chars.append(char)
                    counts.append(count)
                    count = 0
                count += 1
            return chars, counts

        charS, countS = helper(S)
        result = 0
        for word in words:
            charW, countW = helper(word)

            if charS != charW:
                continue

            for cs, cw in zip(countS, countW):
                if cs < cw: break
                if cs > cw and cs < 3: break
            else:
                result += 1

        return result
```
