1239 Maximum Length of a Concatenated String with Unique Characters
===================================================================

Given array of strings, find a maximum length of a string that is
a concatenation of subsequence of the array of strings which have unique
characters.

---

We can perform this task using the hashset structure. Since it is
a subsequence, we can disregard the ordering and consider only for characters
present. 

For each of the string within the given array, we can create a character set
and sift out the string with non-unique characters. Then, for each of these
character set, we create a next set of characters by concatenating it to the
previous character sets via union operation. The newly created set that is
concatenation of previous and current character set, it is considered valid
only if it does not contain any duplicates after concatenation.

---

Python:

```python
class Solution:
    def maxLength(self, arr):
        # sift out all non-unique strings from the given array
        allCharSets = [ set(s) for s in arr if len(set(s)) == len(s) ]
        prevCharSets = [ set() ]

        for currCharSet in allCharSets:
            # concatenate with all the previous character set created thus far
            # note that prevCharSets will be updated; make a copy instead        
            for prevCharSet in prevCharSets.copy():
                nextCharSet = currCharSet | prevCharSet
                # next set of unique characters are valid iff non-duplicate
                if len(nextCharSet) == len(currCharSet) + len(prevCharSet):
                    prevCharSets.append(nextCharSet)

        return len(max(prevCharSets, key=len))
```

