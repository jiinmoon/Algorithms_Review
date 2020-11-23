""" 1.2 Check Permutation

Question:

    Given two strings, write a method to decide if one is a permutation of the
    other.

---

To determine whether the two strings are permuatation of each other, the very
naive approach would be for each char found in the one string, confirm that
there also exists matching char on the other string. Of course, this is a
exhustive search that will require comparing each character against each other;
thus, resulting in suboptimal time complexity of minimum O(n^2).

Further improve upon the algorithm, we can carefully consider the definition of
the permutation; one string is a permutation of another if it is comprised of
exactly equal number of unique characters.

Thus, we can think of two possible improvement. If we wish to save the space,
and is allowed to modifiy the given strings, we can sort the two strings and
compare the two. If two are same, then we can conclude the two strings are
permutation of another. As comparison based sorting takes minimum O(n lg(n))
time complexity, this should take no more than 2 * O(n lg(n)).

Another approach is to employ an extra data structure that can allow us to
record the number of characters that we have seen in each string. While trading
for space, this will result in a linear time complexity.

"""
from collections import Counter

class Solution:

    def checkPermutation_1(self, s1, s2):
        """ sorting approach """
        if not s1 or not s2 or len(s1) != len(s2): return False
        s1, s2 = list(s1), list(s2)
        return sort(s1) == sort(s2)

    def checkPermutation_2(self, s1, s2):
        """ Counter approach (just as good as dict approach) """
        if not s1 or not s2 or len(s1) != len(s2): return False
        counter1 = Counter(s1)
        for ch in s2:
            if counter1.get(ch, -1) == -1:
                return False
            else:
                counter1[ch] -= 1
        return True
