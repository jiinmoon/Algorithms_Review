809 Expressive Words
====================

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

The idea is to have an ordered character groups of chars : count. For example,
"heeelloo" will be turned into:

    "h" : [ "h" ]
    "e" : [ "e", "e", "e" ]
    "l" : [ "l", "l" ]
    "o" : [ "p", "o" ]

Then, we repeat the same procedure with the given words as well. For each word,
we convert them into the same grouping. Then, we can first compare whether they
share the same char groups - if not, then word simply cannot be extended.

If word can be extended, then we take a look at each of its counts against the
given character counts in the S.

Transformation of word --> S is possible if for each of character count in word
and S, count in the S is greater than count in word (or greater than 3 and
more), or the count between word and S should be equal to each other. 

Time complexity should be O(n + m) where n is the length of S and m is the sum
of length of all words.

---

Python:

```python
class Solution:
    def expressiveWords(self, S, words):
        # given a string s
        # return ordered group of char to its counts
        def helper(s):
            chars, counts = list(), list()
            count = 1
            for i, c in enumerate(s):
                if i == len(s)-1 or c != s[i+1]:
                    chars.append(c)
                    counts.append(count)
                    count = 0
                count += 1
            return chars, counts

        charsInS, countsInS = helper(S)

        numStretchy = 0
        for word in Words:
            charsInWord, countsInWord = helper(word)
            
            # cannot stretch word to S if char misalignes
            if charsInWord != charsInS:
                continue
            
            # examine each char count in word and S
            for countW, countS in zip(countsInW, countsInS):
                # cannot have count in Word greater than S
                if countW > countS: break
                # if the count is less, then group size has to be greater than 3
                if countW < countS and countS < 3: break
            else:
                numStretchy += 1

        return numStretchy
```

