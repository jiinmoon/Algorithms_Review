792 Number of Matching Subsequences
===================================

Given string S and a dictionary of words words, find the number of words[i]
that is a subsequence of S.

---

In naive approach, we could take for every word in the words and check whether
it is a subsequence of S.

Better approach would be to maintain a hashmap where the key would be the next
character in the word to be matched with the char in S and value would be the
rest of the body of the word.

For example, suppose that we have words as follows, [a, bb, acd, ace] and the
S of "abcde".

Then, initially, we create a map of head:body as follows:

```
record = { "#" : [ "a", "bb", "acd", "ace" ] }
```

The initial "#" is to start the algorithm. For every character in S, we
retrieve all the bodies of matching char in record. For example, we start with
"#" to retrieve all the bodies to match.

For every body that we examine for current matching character, if it is empty,
then we know that the subsequence of that word is complete and we can increase
the total matching count. Otherwise, we still need more to go: we set the head
as first character of the current body, and next body as the suffix without the
head - and record back.

The time complexity should be O(n + k) where k is the sum of all length of
words and n is the length of S.

---

Python3:

```python
class Solution:
    def numMatchingSubseq(self, S, words):
        # map of word's head : body
        record = collections.defaultdict(list)
        # initial set-up
        record["#"] = words
        count = 0

        for char in "#" + S:
            bodies = record[char]
            # remove to avoid in case of matching char ahead
            del record[char]

            for body in bodies:
                if not body:
                    count += 1
                    continue
                nextHead, nextBody = body[0], body[1:]
                record[nextHead].append(nextBody)
        
        return count
```
