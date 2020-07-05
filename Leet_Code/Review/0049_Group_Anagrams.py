""" 49. Group Anagrams

Question:

    Given an array of strings, group anagrams togeter.

+++

Solution:

    Simplest approach that we can use is utilizing the hash-map structure. For
    the key, we use the sorted word and as a value, the list of words which are
    anagram to the key.

"""
from collections import defaultdict

class Solution:
    def group_anagrams(self, strs):
        d = defaultdict(list)
        for word in strs:
            d[tuple(sorted(word))].append(word)
        return d.values()

