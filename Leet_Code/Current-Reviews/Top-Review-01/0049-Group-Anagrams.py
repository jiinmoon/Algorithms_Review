# 49 Group Anagrams
#
# Use hashmap - as key sort the word and maintain the list of words that share
# same set of characters in that order.

class Solution:
    def groupAnagrams(self, words):
        d = collections.defaultdict(list)
        for word in words:
            d[tuple(sorted(word))].append(word)
        return d.values()
