""" 49. Group Anagrams

Question:

    Given an array of strings, group anagrams together.

+++

Solution:

    As we iterate on the words, we place them into the HashMap structure where
    key is the sorted word - such that we can group the anagrams.

"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        result = defaultdict(list)
        for word in strs:
            result[tuple(sorted(word))].append(word)
        return result.values()
