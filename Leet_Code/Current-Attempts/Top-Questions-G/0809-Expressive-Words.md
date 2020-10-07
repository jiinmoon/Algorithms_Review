# 809 Expressive Words

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

To find whether given word can be "stretched" to form string S, we need to
examine each character and its repeated counts at the each apperance. For
example, if the string S is "helllllooo", it should be converted into "h" 1, 
"e" 1, "l" 5, and "o" 3.

Then, for each word, we repeat the same process. First, we chck for correct
order as well as composition of the characters in the string S and word. Then,
we check the count of each character as they appear - if character from word
contains more character than S, we cannot stretch it. If the count is less, we
should also need to check for whether the size of the group is less than 3.

---

Python:

```python

class Solution:
    def expressiveWords(self, words, S):
        def helper(word):
            chars, counts = list(), list()
            count = 1
            for i, char in enumerate(S):
                if i == len(S) - 1 or char != S[i+1]:
                    chars.append(char)
                    counts.append(count)
                    count = 0
                count += 1
            return chars, count

        charS, countS = helper(S)
        total = 0

        for word in words:
            charW, countW = helper(word)

            if charW != charW:
                continue

            for cw, cs in zip(countW, countS):
                if cw > cs: break
                if cw < cs and cs < 3: break
            else:
                total += 1

        return total
```
