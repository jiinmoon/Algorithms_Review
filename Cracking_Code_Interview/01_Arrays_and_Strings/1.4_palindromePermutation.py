""" 1.4 Plaindrome Permutation

Question:

    Given a string, write a function to check if it is a permutation of a
    plaindrome. A paldinrome is a word or phrase that is the same forwards and
    backwards. A permutation is a rearrangement of letters. The palindrome does
    not need to be limited to just dictionary words.

---

At first glance, this appears to be a difficult task. In naive approach, it
almost as if we have to create every permutation (rearranement) of the given
string, then check whether it is a plaindrome or not. This is a very extensive
algorithm and expensive one.

Thus, we will have to think differently about the subject. Is there some quality
about the permutation and palindrome that we can exploit?

As it turns out, we can use the fact that every palindrome is composed of zero,
or single odd number of unique char, and any number of even number of characters.

i.e. 'aabaa' = 4a 1b = even number of 'a' and single odd number of 'b' = True
i.e. 'aabcaa' = 4a 1b 1c = even number of 'a', but two odd number of 'b' and 'c'

Thus, the problem simply requires us to linearly scan the entire string once to
counter the number of characters to assess the number of unique characters
occurrences to determine whether the original string can be the permutation of
the palindrome or not.

The improvement would be checking as we go; using the early exit strategy -
we count the number of odd instance; found another odd instance? return False asap.

There is also an Bit-Manipulation method which is to be further explored.

"""

from collections import Counter

class Solution:

    def palindromePermutation(self, s):
        if not s: return s
        c = Counter(s)
        foundOdd = False
        for ch, num in c.items():
            if num % 2 != 0: # odd found
                if foundOdd: # we already previously found odd
                    return False
                foundOdd = True
        return True
