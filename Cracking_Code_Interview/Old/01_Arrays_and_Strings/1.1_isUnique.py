""" 1.1 Is Unique

Question:

    Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structure?

---

To identify whether a given string is only comprised of unique characters, the
first naive approach would be the comparing all characters against each other at
every position. This is obviously not a desirable algorithm as its time
complexity would be O(n^2).

The improvement would be sort the string alphabetically, and then check for
duplicate characters in the neighbours. This would be at best O(n lg(n)) time
complexity unless we know something about that data that we can exploit prior to
it. Also, this method can satisfy the non-additional data structure clause iff
sorting can take in-place and we are allowed to fix the original string.

THe noble linear time solution is to count the number of characters in the given
string and record it in fast look-up data structure such as Dictionary
(hashmap).

"""

class Solution:
    def isUnique_1(self, s):
        """ naive implementaion that compares each char against every other
        position. """
        if not s: return False
        for i in range(len(s)-1):
            for j in range(i, len(s)-1):
                currChar, compChar = s[i], s[j]
                if currChar == compChar: return False
        return True

    def isUnique_2(self, s):
        """ Sorting method. """
        if not s: return False
        s = list(s)
        return len(set(s)) == len(s)

    def isUnique_3(self, s):
        """ Dictionary approach. """
        if not s: return False
        charMap = {}
        for char in s:
            if charMap.get(char, -1) == -1:
                charMap[char] = 1
            else:
                return False
        return True


